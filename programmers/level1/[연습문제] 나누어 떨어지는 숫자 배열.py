# [연습문제] 나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = [a for a in arr if a % divisor == 0]
    answer.sort()
    if not answer: return [-1]
    return answer
    # return answer or [-1]

if __name__ == "__main__":
    print(solution([5, 9, 7, 10], 5) == [5, 10])
    print(solution([2, 36, 1, 3], 1) == [1, 2, 3, 36])
    print(solution([3,2,6], 10) == [-1])