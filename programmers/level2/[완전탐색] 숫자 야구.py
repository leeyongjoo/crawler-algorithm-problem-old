# [완전탐색] 숫자 야구
def solution(baseball):
    answer = []
    for a in range(123, 988):
        ans = str(a)
        if '0' in ans or len(set(ans)) < 3:
            continue

        flag = True
        for nsb in baseball:
            num, strk, ball = nsb
            comp = str(num)
            s_cnt, b_cnt = 0, 0
            for i in range(len(comp)):
                if comp[i] == ans[i]:
                    s_cnt += 1
                elif comp[i] in ans:
                    b_cnt += 1
            if s_cnt != strk or b_cnt != ball:
                flag = False
                break

        if flag is True:
            answer.append(int(ans))
    return len(answer)

if __name__ == "__main__":
    print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))
    print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]) == 2)
