# [탐욕법(Greedy)] 조이스틱
def solution(name):
    from string import ascii_uppercase as alpha
    updown_list = []
    for a in name:
        i = alpha.index(a)
        updown_list.append(min(i, len(alpha) - i))

    idx, count_move = 0, 0
    while True:
        count_move += updown_list[idx]
        updown_list[idx] = 0

        if sum(updown_list) == 0:
            break

        left, right = 1, 1
        while updown_list[idx - left] == 0:
            left += 1
        while updown_list[idx + right] == 0:
            right += 1

        if left < right:
            idx -= left
            count_move += left
        else:
            idx += right
            count_move += right
    return count_move

if __name__ == "__main__":
    print(solution("JAZ"))
    print(solution("JEROEN"))
    print(solution("JEROEN") == 56)
    print(solution("JAN"))
    print(solution("JAN") == 23)
    print(solution("BBABAAAB"))