# [스택큐] 기능개발
def solution(progresses, speeds):
    from math import ceil
    from collections import deque
    deployable_time = deque()
    for p, s in zip(progresses,speeds):
        deployable_time.append(ceil((100 - p)/s))

    deploy_per_day = []
    while deployable_time:
        first = deployable_time.popleft()
        per_day = 1
        while deployable_time and first >= deployable_time[0]:
            deployable_time.popleft()
            per_day += 1
        deploy_per_day.append(per_day)
    return deploy_per_day
    
if __name__ == "__main__":
    print(solution([93,30,55], [1,30,5]))
    print(solution([93,30,55], [1,30,5]) == [2,1])