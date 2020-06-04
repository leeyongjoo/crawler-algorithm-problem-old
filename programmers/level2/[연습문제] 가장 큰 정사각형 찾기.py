# [연습문제] 가장 큰 정사각형 찾기
def solution(board):
    dp = board.copy()
    for i in range(1, len(dp[1:])+1):
        for j in range(1, len(dp[0][1:])+1):
            if dp[i][j] > 0:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
    return max([col for row in dp for col in row])**2

if __name__ == "__main__":
    print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
    # print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]) == 9)
    print(solution([[0,0,1,1],[1,1,1,1]]))
    # print(solution([[0,0,1,1],[1,1,1,1]]) == 4)