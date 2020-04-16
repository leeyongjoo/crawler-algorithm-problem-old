# [2019 카카오 개발자 겨울 인턴십] 크레인 인형뽑기 게임
def solution(board, moves):
    stack = []
    popped_count = 0
    for m in moves:
        bIdx = m-1
        for b in board:
            if b[bIdx] != 0:
                if stack and stack[-1] == b[bIdx]:
                    stack.pop()
                    popped_count += 2
                else:
                    stack.append(b[bIdx])
                b[bIdx] = 0
                break
    return popped_count
    
if __name__ == "__main__":
    print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
    print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]) == 4)