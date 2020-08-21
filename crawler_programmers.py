from bs4 import BeautifulSoup
from modules.module_string import remove_win_special_char
from modules.module_path import *
from modules.JSONManager import JSONManager
import requests
import urllib

SITE_NAME = 'programmers'
SITE_URL = 'https://programmers.co.kr'
SITE_PROBLEMS_URL = '/'.join([SITE_URL, 'learn', 'challenges'])
CONFIG_KEYS = [
    'language',  # 언어
]
params = {
    'tab': 'all_challenges',
    'page': 1,
}


def crawling_problem():
    """
    * json 파일로 level, language에 대한 기본값 설정
    1. 설정한 기본값에 대한 문제 크롤링
    2. 파일로 저장


    :return:
    """
    # p_level = input('input Problem Level\n>> ')
    # p_url = input('Input Problem URL\n>> ').replace(' ', '')
    # if '?language=python3' not in p_url:
    #     p_url = ''.join([p_url, "?language=python3"])

    jm = JSONManager(SITE_NAME, CONFIG_KEYS)
    problem_language = jm.get_json_data()['language']

    while True:
        problems_url = '?'.join([SITE_PROBLEMS_URL, urllib.parse.urlencode(params)])
        html = requests.get(problems_url).text
        soup = BeautifulSoup(html, 'lxml')

        problems = soup.select('#tab_all_challenges > section > div > div.challenge__algorithms--index.col-md-8 '
                                   '> div.algorithm-list > div.row > div')
        if problems:
            print(f"{params['page']} 페이지 시작.")
        else:
            break

        for problem in problems:
            # 해당 문제가 지정한 언어를 제공하는 지 검사
            try:
                problem_path = problem.find('div', {'data-original-title': problem_language}).find('a').get('href')
            except AttributeError:  # 해당 언어가 없을 경우
                continue

            problem_level = problem.find('div').get('class')[1].split('-')[1]
            problem_title = problem.find('h4').get_text()
            problem_category = problem.find('h6').get_text()

            problem_url = ''.join([SITE_URL, problem_path])
            # language 추가해서 돌림
            file_content = make_file_content(problem_url)
            filename = '[{}] {}'.format(problem_category, problem_title)

            # 파일 이름에 특수문자 제거
            filename = remove_win_special_char(filename)
            file = join_path(f"{SITE_NAME}", f"level{problem_level}", filename + get_extension(problem_language))

            if is_file(file):
                print(f"{filename}은 이미 존재합니다!")
            else:
                mkdir_if_not_exists(get_file_dirname(file))
                with open(file, 'w', encoding='utf-8') as f:
                    f.writelines(a + '\n' for a in [
                        ''.join(['# ', filename]),
                        ''.join(['# ', problem_url]),
                        file_content,
                    ])
                print(file, '생성 완료')

        params['page'] = params['page'] + 1
        break


def make_file_content(PROBLEMS_URL):
    html = requests.get(PROBLEMS_URL).text
    soup = BeautifulSoup(html, 'lxml')

    # <q> 태그를 " 문자로 변환
    for q in soup.findAll('q'):
        text = q.get_text()
        q.replaceWith('"{}"'.format(text))

    # 코드
    code = soup.select_one('#code').get_text()

    # 입출력 예
    p_input_list = []
    p_output_list = []

    try:
        p_example_table = soup.select('#tour2 > div > div > table')[-1]
    except IndexError:
        test_code_list = 'pass'
    else:
        p_example_tr_list = p_example_table.select('tbody > tr')
        p_example_td_list = [e.find_all('td') for e in p_example_tr_list]

        for *i, o in p_example_td_list:
            p_input_list.append([a.get_text() for a in i])
            p_output_list.append(o.get_text())

        # output 중에서 bool 타입은 capitalize
        for i, s in enumerate(p_output_list):
            if s in ['true', 'false']:
                p_output_list[i] = s.capitalize()

        # 테스트 코드는 마지막 테이블만..
        test_code_list = []
        for i, o in zip(p_input_list, p_output_list):
            test_code_list.append('print(solution({}))'.format(', '.join(i)))
            test_code_list.append('print(solution({}) == {})'.format(', '.join(i), o))

    test_code = f'\n{" "*4}'.join(test_code_list)

    # 파일 내용
    file_content = f'{code}\n\nif __name__ == "__main__":\n{" "*4}{test_code}'
    return file_content


def main():
    crawling_problem()


if __name__ == "__main__":
    main()