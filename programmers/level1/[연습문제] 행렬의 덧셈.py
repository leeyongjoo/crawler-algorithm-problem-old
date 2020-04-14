# [연습문제] 행렬의 덧셈
def solution(arr1, arr2):
    col_len = len(arr1[0]) # 열의 크기가 동일
    arr = []
    for a, b in zip(arr1, arr2):
        row = []
        for x, y in zip(a, b):
            row.append(x + y)
        arr.append(row)
    return arr
    
if __name__ == "__main__":
    print(solution([[1,2],[2,3]], [[3,4],[5,6]]))
    print(solution([[1,2],[2,3]], [[3,4],[5,6]]) == [[4,6],[7,9]])
    print(solution([[1],[2]], [[3],[4]]))
    print(solution([[1],[2]], [[3],[4]]) == [[4],[6]])