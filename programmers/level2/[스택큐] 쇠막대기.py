# [스택큐] 쇠막대기
def solution(arrangement):
    stack = []
    count_stick = 0
    prev = ''
    for a in arrangement:
        if a == '(':
            stack.append(a)
        else:
            if prev == '(':
                stack.pop()
                count_stick += len(stack)
            else:
                stack.pop()
                count_stick += 1
        prev = a
    return count_stick

if __name__ == "__main__":
    print(solution("()(((()())(())()))(())"))
    print(solution("()(((()())(())()))(())") == 17)