# [완전탐색] 카펫
def solution(brown, yellow):
    xy_mul = brown + yellow
    for y in range(1, int(xy_mul**.5) + 1):
        if xy_mul % y == 0:
            x = int(xy_mul / y)
            if (x-2) * (y-2) == yellow:
                return [x, y]
    return [-1, -1]
    
if __name__ == "__main__":
    print(solution(10, 2))
    print(solution(10, 2) == [4, 3])
    print(solution(8, 1))
    print(solution(8, 1) == [3, 3])
    print(solution(24, 24))
    print(solution(24, 24) == [8, 6])