# [탐욕법(Greedy)] 큰 수 만들기
def solution(number, k):
    digits_num = len(number) - k
    start, end = 0, k + 1
    result = []
    for _ in range(digits_num):
        sliced_num = number[start:end]
        nine_index = sliced_num.find('9')
        if nine_index > -1:
            max_num = '9'
            start += nine_index + 1
        else:
            max_num = max(sliced_num)
            start += sliced_num.index(max_num) + 1
        end += 1
        result.append(max_num)
    return ''.join(result)

# 다른 풀이
def solution(number, k):
    stack = []
    for a in number:
        while stack and stack[-1] < a and k > 0:
            k -= 1
            stack.pop()
        stack.append(a)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)

if __name__ == "__main__":
    # print(solution("1924", 2))
    # print(solution("1924", 2) == "94")
    print(solution("1231234", 3))
    # print(solution("1231234", 3) == "3234")
    # print(solution("4177252841", 4))
    # print(solution("4177252841", 4) == "775841")