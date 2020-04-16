# [SummerWinter Coding(~2018)] 예산
def solution(d, budget):
    d.sort()
    sup_count = 0
    for a in d:
        if a <= budget:
            budget -= a
            sup_count += 1
        else:
            break
    return sup_count
    
if __name__ == "__main__":
    print(solution([1,3,2,5,4], 9))
    print(solution([1,3,2,5,4], 9) == 3)
    print(solution([2,2,3,3], 10))
    print(solution([2,2,3,3], 10) == 4)