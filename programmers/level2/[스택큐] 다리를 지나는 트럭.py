# [스택큐] 다리를 지나는 트럭
def solution(bridge_length, weight, truck_weights):
    q = []
    used_weight = 0
    time_count = 0

    while True:
        time_count += 1
        for a in q:
            a[1] += 1

        if q and q[0][1] == bridge_length:
            used_weight -= q.pop(0)[0]

        if not (q or truck_weights):
            break

        if truck_weights and used_weight + truck_weights[0] <= weight:
            tw1 = truck_weights.pop(0)
            q.append([tw1, 0])
            used_weight += tw1
    return time_count

if __name__ == "__main__":
    print(solution(2, 10, [7,4,5,6]))
    print(solution(2, 10, [7,4,5,6]) == 8)
    print(solution(100, 100, [10]))
    print(solution(100, 100, [10]) == 101)
    print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
    print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]) == 110)