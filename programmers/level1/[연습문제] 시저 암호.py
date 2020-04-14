# [연습문제] 시저 암호
def solution(s, n):
    from string import ascii_lowercase as low
    from string import ascii_uppercase as upp

    answer = []
    for c in s:
        if c in low:
            answer.append(low[(low.index(c)+n)%len(low)])
        elif c in upp:
            answer.append(upp[(upp.index(c)+n)%len(upp)])
        else:
            answer.append(c)
    return ''.join(answer)
    
if __name__ == "__main__":
    print(solution("AB", 1) == "BC")
    print(solution("z", 1) == "a")
    print(solution("a B z", 4) == "e F d")