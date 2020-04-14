# [연습문제] 이상한 문자 만들기
def solution(s):
    before_word_list = s.split(' ')
    after_word_list = []
    for bw in before_word_list:
        c_list = []
        for i, c in enumerate(bw):
            if i % 2 == 0:
                c_list.append(c.upper())
            elif i % 2 == 1:
                c_list.append(c.lower())
        after_word_list.append(''.join(c_list))
    return ' '.join(after_word_list)

if __name__ == "__main__":
    print(solution("try hello world") == "TrY HeLlO WoRlD")