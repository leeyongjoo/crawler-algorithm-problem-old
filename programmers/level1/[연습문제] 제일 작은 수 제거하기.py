# [연습문제] 제일 작은 수 제거하기
def solution(arr):
    min_arr = min(arr)
    removed_min = [a for a in arr if a > min_arr]
    return removed_min or [-1]
    
if __name__ == "__main__":
    print(solution([4,3,2,1]) == [4,3,2])
    print(solution([10]) == [-1])