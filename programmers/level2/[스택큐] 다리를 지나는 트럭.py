# [스택큐] 다리를 지나는 트럭
def solution(bridge_length, weight, truck_weights):
    q = []
    bw = 0
    time = 0

    while True:
        time += 1
        for a in q:
            a[1] += 1

        if q and q[0][1] == bridge_length:
            bw -= q.pop(0)[0]

        if not (q or truck_weights):
            break

        if truck_weights and bw + truck_weights[0] <= weight:
            tw = truck_weights.pop(0)
            q.append([tw, 0])
            bw += tw
    return time


    
if __name__ == "__main__":

    print(solution(2, 10, [7,4,5,6]))
    print(solution(2, 10, [7,4,5,6]) == 8)
    print(solution(100, 100, [10]))
    print(solution(100, 100, [10]) == 101)
    print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
    print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]) == 110)