# [스택큐] 탑
def solution(heights):
    answer = [0] * len(heights)
    stack = []
    for i in range(len(heights)-1, -1, -1):
        while stack and heights[stack[-1]] < heights[i]:
            answer[stack.pop()] = i + 1
        stack.append(i)
    return answer
    
if __name__ == "__main__":
    # print(solution([6,9,5,7,4]))
    print(solution([6,9,5,7,4]) == [0,0,2,2,4])
    print(solution([6,9,5,1,4]))
    # print(solution([3,9,9,3,5,7,2]))
    # print(solution([3,9,9,3,5,7,2]) == [0,0,0,3,3,3,6])
    # print(solution([1,5,3,6,7,6,5]))
    # print(solution([1,5,3,6,7,6,5]) == [0,0,2,0,0,5,6])