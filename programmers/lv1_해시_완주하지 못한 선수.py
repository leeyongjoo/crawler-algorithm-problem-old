def solution(participant, completion):
    completionDict = {}

    for p in participant:
        completionDict.setdefault(p, 0)
        completionDict[p] += 1

    for c in completion:
        completionDict[c] -= 1

    for k, v in completionDict.items():
        if v > 0:
            return k
        elif v < 0:
            print(k, "의 완주인원이 참가인원보다 많음")
            return ''
    return ''

# 다른 사람의 풀이
def solution(participant, completion):
    import collections

    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

if __name__ == "__main__":
    print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))