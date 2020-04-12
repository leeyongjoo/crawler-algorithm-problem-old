# [연습문제] 서울에서 김서방 찾기
def solution(seoul):
    return '김서방은 {}에 있다'.format(seoul.index('Kim'))
    
if __name__ == "__main__":
    print(solution(["Jane", "Kim"]) == "김서방은 1에 있다")