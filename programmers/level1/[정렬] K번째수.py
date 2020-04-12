# [정렬] K번째수
def solution(array, commands):
    answer = []
    for command in commands:
        start, end, index = [a-1 for a in command]
        array_command = array[start:end+1]
        array_command.sort()
        answer.append(array_command[index])
    return answer
    
if __name__ == "__main__":
    print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]) == [5, 6, 3])