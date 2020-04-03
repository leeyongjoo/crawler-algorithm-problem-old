# [탐욕법(Greedy)] 체육복
def solution1(n, lost, reserve):
    lendable_list = list(set(reserve).difference(set(lost)))
    stolen_list = list(set(lost).difference(set(reserve)))
    wearable_num = n-len(stolen_list)
    for i, l in enumerate(stolen_list):
        if l-1 in lendable_list:
            wearable_num+=1
            lendable_list.remove(l-1)
        elif l+1 in lendable_list:
            wearable_num+=1
            lendable_list.remove(l+1)
    return wearable_num

# 다시 풀기
def solution2(n, lost, reserve):
    lendable_list = [r for r in reserve if r not in lost]
    stolen_list = [l for l in lost if l not in reserve]

    for lendable in lendable_list:
        front = lendable - 1
        back = lendable + 1
        if front in stolen_list:
            stolen_list.remove(front)
        elif back in stolen_list:
            stolen_list.remove(back)
    return n-len(stolen_list)
    
if __name__ == "__main__":
    import time
    start = time.time()
    for _ in range(100000):
        solution2(5, [2, 4], [1, 3, 5])
        solution2(5, [2, 4], [3])
        solution2(3, [3], [1])
        solution2(5, [2,4], [3,5])
    print(time.time() - start)

    start = time.time()
    for _ in range(100000):
        solution1(5, [2, 4], [1, 3, 5])
        solution1(5, [2, 4], [3])
        solution1(3, [3], [1])
        solution1(5, [2, 4], [3, 5])
    print(time.time() - start)