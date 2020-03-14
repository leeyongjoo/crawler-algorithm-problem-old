import requests, lxml
from bs4 import BeautifulSoup

CODEUP_URL = 'https://codeup.kr/'

def crawler_codeup_problemset():
    problemsets_dict = {}

    html = requests.get(CODEUP_URL + 'problemsetsol.php').text
    soup = BeautifulSoup(html, 'lxml')
    problemsets_tags_a = soup.select('body > main > div > div > div.col-4 > div > a')

    for problemset_a in problemsets_tags_a:
        problemsets_dict[problemset_a.get_text()] = problemset_a.get('href')

    # for i, k in enumerate(problemsets_dict):
    #     print('[{:0>2}] {:}'.format(i, k))

    # while True:
    #     #     try:
    #     #         problemset_index = int(input("문제집 선택 >> "))
    #     #         break
    #     #     except Exception as e:
    #     #         pass

    problemset_index = 0
    problemset_url = CODEUP_URL + problemsets_dict[tuple(problemsets_dict.keys())[problemset_index]]

    html_problemset = requests.get(problemset_url).text
    soup_problemset = BeautifulSoup(html_problemset, 'lxml')
    problems = soup_problemset.select('#problemset > tbody > tr')

    for problem in problems:
        num = problem.select_one('td:nth-child(2) > div').get_text()
        name = problem.find('a').get_text().replace('(설명)','')
        print('_'.join([num, name]))

    # 기초 100제




if __name__ == "__main__":
    crawler_codeup_problemset()