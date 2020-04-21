# [연습문제] 124 나라의 숫자
def solution(n):
    lang = '124'
    lang_len = len(lang)
    remainder_list = []
    while n:
        n -= 1
        remainder_list.append(lang[n % lang_len])
        n //= lang_len
    return ''.join(remainder_list[::-1])

if __name__ == "__main__":
    print(solution(1))
    print(solution(2))
    print(solution(3))
    print(solution(4))
    print(solution(5))
    print(solution(6))
    print(solution(11))


