# [연습문제] 올바른 괄호
def solution(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
    return stack == []
    
if __name__ == "__main__":
    print(solution("()()"))
    print(solution("()()") == True)
    print(solution("(())()"))
    print(solution("(())()") == True)
    print(solution(")()("))
    print(solution(")()(") == False)
    print(solution("(()("))
    print(solution("(()(") == False)