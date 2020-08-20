from bs4 import BeautifulSoup
from selenium import webdriver, common
from modules.LoginManager import LoginManager
from modules.module_path import join_path, get_file_dirname, get_file_list, mkdir_if_not_exists
from modules.module_string import remove_win_special_char

SITE_URL = 'https://codeup.kr/'
SITE_NAME = 'codeup'
SITEMAP = {
    'login': 'loginpage.php',
    'problemsetsol': 'problemsetsol.php',
    'problem': 'problem.php',
}


def crawling_solved_problem():
    # 브라우저 실행
    browser = webdriver.Chrome()
    # 페이지 로딩 시간 설정(seconds)
    browser.implicitly_wait(5)

    ##########
    # 로그인 #
    ##########
    lm = LoginManager(SITE_NAME)
    login_page = join_path(SITE_URL, SITEMAP['login'])
    browser.get(login_page)
    while True:
        user_id, user_pw = lm.get_idpw_from_json()
        browser.find_element_by_css_selector(
            'body > div.container.mt-5.mb-5 > form > div:nth-child(2) > input').send_keys(user_id)
        browser.find_element_by_css_selector(
            'body > div.container.mt-5.mb-5 > form > div:nth-child(3) > input').send_keys(user_pw)
        browser.find_element_by_css_selector(
            'body > div.container.mt-5.mb-5 > form > input').click()
        try:
            # 로그인 후 문제집 페이지 가져오기
            problemsetsol_page = join_path(SITE_URL, SITEMAP['problemsetsol'])
            browser.get(problemsetsol_page)
        # 로그인 오류
        except common.exceptions.UnexpectedAlertPresentException as e:
            print(e.alert_text)
            lm.write_and_load()
            browser.find_element_by_css_selector(
                'body > div.container.mt-5.mb-5 > form > div:nth-child(2) > input').clear()
            browser.find_element_by_css_selector(
                'body > div.container.mt-5.mb-5 > form > div:nth-child(3) > input').clear()
        else:
            break

    html = browser.page_source
    # 문제집 선택하고, 선택한 문제집의 name과 url 반환
    problemset_name, problemset_url = select_problemset_and_get_problemset_name_and_url(html)

    # 선택한 문제집 페이지 접속
    browser.get(problemset_url)

    html = browser.page_source
    # 해결한 문제 리스트 가져오기
    solved_problems_id_name: list = get_solved_problem_list_from_html(html)

    # 반복문 돌기 전에 이미 가져와서 저장된 문제를 리스트에서 제외
    saved_problems_file_name: list = get_file_list(
        join_path(get_file_dirname(__file__), SITE_NAME, problemset_name))
    saved_problems_id: list = [file_name.split('_')[0] for file_name in saved_problems_file_name]

    solved_problems_id_name_not_saved = [
        id_name for id_name in solved_problems_id_name if id_name[0] not in saved_problems_id
    ]
    if solved_problems_id_name_not_saved:
        print(f'{len(solved_problems_id_name_not_saved)} 문제 저장을 시작합니다.')
    else:
        print('문제가 이미 저장되어 있습니다.')

    # 반복문으로 문제 리스트 돌면서 browser로 소스코드 가져오기
    problem_url = join_path(SITE_URL, SITEMAP['problem'])
    for problem_id, problem_name in solved_problems_id_name_not_saved:
        problem_url_with_id = f'{problem_url}?id={problem_id}'
        browser.get(problem_url_with_id)

        # 내 소스1
        my_source1_href = browser.find_element_by_css_selector(
            'body > main > div > div:nth-child(6) > div.card-header > a.btn-primary').get_attribute('href')

        browser.get(my_source1_href)
        problem_source_code = browser.find_element_by_css_selector('#source > div.ace_scroller').text

        # 문제집 명/id_name으로 파일 저장
        file_name = '_'.join([problem_id, remove_win_special_char(problem_name)])

        mkdir_if_not_exists(join_path(get_file_dirname(__file__), SITE_NAME, problemset_name))

        file = join_path(
            get_file_dirname(__file__), SITE_NAME, problemset_name, file_name
        )
        file = ''.join([file, '.py'])
        first_line = '# ' + ' : '.join([problem_id, problem_name]) + '\n'
        try:
            with open(file, 'w', encoding='utf-8') as f:
                # 첫줄에 주석으로 아이디, 문제 이름 추가
                f.write(first_line)
                f.write(problem_source_code)
        # 파일명에 '/'가 들어간 경우 or 파일명이 너무 긴경우(python path length limit)
        except FileNotFoundError as e:
            print('FileNotFoundError', e)
        except OSError as e:
            print('OSError', e)
        else:
            print(file, '저장 완료.')
    browser.quit()


def select_problemset_and_get_problemset_name_and_url(html):
    """
    콘솔에 문제집 리스트 출력하여 선택받고 선택한 문제집의 name, url 반환

    :param html: page_source
    :return: name(str), url(str)
    """
    problemsets_tags_a = get_problemsets_tags_a_from_html(html)
    print_problemsets_tags_a(problemsets_tags_a)
    problemset = get_problemset_by_selecting(problemsets_tags_a)

    problemset_name = problemset.get_text()
    problemset_url = join_path(SITE_URL, problemset.get('href'))
    return problemset_name, problemset_url


def get_problemsets_tags_a_from_html(html):
    soup = BeautifulSoup(html, 'lxml')
    problemsets_tags_a = soup.select('body > main > div > div > div.col-4 > div > a')
    return problemsets_tags_a


def print_problemsets_tags_a(tags_a):
    for i, a in enumerate(tags_a):
        print(f'[{i:0>2}] {a.get_text()}')


def get_problemset_by_selecting(tags_a):
    while True:
        try:
            problemset_index = int(input("문제집 선택 >> "))
            problemset = tags_a[problemset_index]
        except IndexError:
            print(f'0~{len(tags_a)} 이내의 번호를 입력하세요!')
        except ValueError:
            print(f'숫자를 입력하세요!')
        else:
            return problemset


def get_solved_problem_list_from_html(html):
    soup = BeautifulSoup(html, 'lxml')
    problem_tags_tr = soup.select('#problemset > tbody > tr')

    solved_problem_list = []
    for problem_tr in problem_tags_tr:
        if problem_tr.select_one('td:nth-child(1) > div').get_text() == 'Y':  # 해결한 문제만 추출
            problem_id = problem_tr.select_one('td:nth-child(2) > div').get_text()
            problem_name = problem_tr.select_one('td:nth-child(3) > div').get_text()
            solved_problem_list.append((problem_id, problem_name))
    return solved_problem_list


def main():
    crawling_solved_problem()


if __name__ == "__main__":
    main()
