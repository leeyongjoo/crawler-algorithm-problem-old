# [연습문제] 정수 내림차순으로 배치하기
def solution(n):
    n_list = [a for a in str(n)]
    n_list.sort(reverse=True)
    return int(''.join(n_list))
    
if __name__ == "__main__":
    print(solution(118372) == 873211)