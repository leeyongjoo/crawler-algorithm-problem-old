# [2019 KAKAO BLIND RECRUITMENT] 실패율
def solution(N, stages):
    stages.sort()
    challengers_num = len(stages)
    stages_dd = {}
    for n in range(1, N + 1):
        stages_dd[n] = 0
    for stage in stages:
        if stage <= N:
            stages_dd[stage] += 1

    failureRate = {}
    for k, v in stages_dd.items():
        if challengers_num:
            failureRate[k] = v / challengers_num
        else:
            failureRate[k] = 0
        challengers_num -= v

    return [a[0] for a in sorted(failureRate.items(), key=lambda x: x[1], reverse=True)]


# 다른 사람의 풀이
def solution(N, stages):
    failureRate = {}
    challengersNum = len(stages)
    for stage in range(1, N + 1):
        if challengersNum > 0:
            failureCount = stages.count(stage)
            failureRate[stage] = failureCount/challengersNum
            challengersNum -= failureCount
        else:
            failureRate[stage] = 0
    return sorted(failureRate, key=lambda x: failureRate[x], reverse=True)


if __name__ == "__main__":
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]) == [3, 4, 2, 1, 5])
    print(solution(4, [4, 4, 4, 4, 4]))
    print(solution(4, [4, 4, 4, 4, 4]) == [4, 1, 2, 3])
