# [연습문제] 같은 숫자는 싫어
def solution(arr):
    answer = []
    answer.append(arr[0])
    for a in arr[1:]:
        if a != answer[-1]:
            answer.append(a)
    return answer
    
if __name__ == "__main__":
    print(solution([1,1,3,3,0,1,1]) == [1,3,0,1])
    print(solution([4,4,4,3,3]) == [4,3])