import requests, selenium, lxml
from bs4 import BeautifulSoup
import json

import selenium.webdriver

CODEUP_URL = 'https://codeup.kr/'

# TODO : 일단 함수안에 함수 넣었는데 나중에 따로 빼놓기
def crawling_solved_problem():

    def login_codeup():
        try:
            with open('login_info/codeup_login.json') as f:
                json_data = json.load(f)
        except Exception as e:
            print('로그인 정보 파일 오류!')
            print(e)
            return None
        else:
            return json_data
    login_json_data = login_codeup()
    CODEUP_ID, CODEUP_PW = login_json_data['userId'], login_json_data['userPw']

    # use Chrome webdriver
    browser = selenium.webdriver.Chrome("./driver/chromedriver.exe")
    # wait 5 minutes
    browser.implicitly_wait(5)

    # login
    browser.get('https://codeup.kr/loginpage.php')
    browser.find_element_by_css_selector('body > div.container.mt-5.mb-5 > form > div:nth-child(2) > input').send_keys(CODEUP_ID)
    browser.find_element_by_css_selector('body > div.container.mt-5.mb-5 > form > div:nth-child(3) > input').send_keys(CODEUP_PW)

    try:
        browser.find_element_by_css_selector('body > div.container.mt-5.mb-5 > form > input').click()
    except selenium.common.exceptions.UnexpectedAlertPresentException as e:
        print(e)
        # TODO : 콘솔로 ID, PW  다시 요청
        return -1

    # get problemset page
    # 문제집 페이지 가져오기
    browser.get(CODEUP_URL + 'problemsetsol.php')
    html = browser.page_source

    # select problemset
    # 문제집 선택
    problemset_name, problemset_url = select_problemset_and_get_name_and_url(html)

    # get selected problemset page
    # 선택한 문제집 페이지 접속
    browser.get(problemset_url)
    html = browser.page_source

    def get_solved_problem_dict_list(html):
        soup = BeautifulSoup(html, 'lxml')
        problem_tags_tr = soup.select('#problemset > tbody > tr')

        solved_problem_dict_list = []
        for problem_tr in problem_tags_tr:
            problem_dict = {}
            if problem_tr.select_one('td:nth-child(1) > div').get_text() == 'Y':
                problem_dict['id'] = problem_tr.select_one('td:nth-child(2) > div').get_text()
                problem_dict['name'] = problem_tr.select_one('td:nth-child(3) > div').get_text().replace('(설명)', '')
                solved_problem_dict_list.append(problem_dict)
        return solved_problem_dict_list

    # get solved problem list
    # 해결한 문제의 id 리스트 가져오기
    solved_problem_dict_list = get_solved_problem_dict_list(html)

    print()

    # TODO: 반복문으로 맞춘 문제 리스트 돌면서 selenium으로
    #  예)https://codeup.kr/problem.php?id=1001 처럼 들어가서 소스코드 가져오기
    problem_url_prefix = 'https://codeup.kr/problem.php?id='
    for problem_dict in solved_problem_dict_list:
        problem_id = problem_dict['id']
        problem_name = problem_dict['name']
        browser.get(problem_url_prefix + problem_id)

        my_source1_href = browser.find_element_by_css_selector(
            'body > main > div > div:nth-child(6) > div.card-header > a.btn-primary').get_attribute('href')

        browser.get(my_source1_href)
        problem_source_code = browser.find_element_by_css_selector('#source > div.ace_scroller').text

        # 문제집 명/id_name으로 파일 저장
        problem_info = '_'.join([problem_id, problem_name])
        # TODO: 'codeup/'+problemset_name 폴더 있는지 확인 후 없으면 생성

        filename = '/'.join(['codeup', problemset_name, problem_info])
        filename = ''.join([filename,'.py'])

        with open(filename, 'w') as f:
            f.write(problem_source_code)

    browser.quit()


def select_problemset_and_get_name_and_url(html):
    soup = BeautifulSoup(html, 'lxml')
    problemsets_tags_a = soup.select('body > main > div > div > div.col-4 > div > a')

    problemsets_dict = {}
    for problemset_a in problemsets_tags_a:
        problemsets_dict[problemset_a.get_text()] = problemset_a.get('href')

    for i, k in enumerate(problemsets_dict):
        print('[{:0>2}] {:}'.format(i, k))

    while True:
        try:
            problemset_index = int(input("문제집 선택 >> "))
            break
        except Exception as e:
            pass

    problemset_name = tuple(problemsets_dict.keys())[problemset_index]
    problemset_url = CODEUP_URL + problemsets_dict[problemset_name]
    return problemset_name, problemset_url

if __name__ == "__main__":
    crawling_solved_problem()
    pass