# [연습문제] 2016년
def solution(a, b):
    num_dayOfMonth = [31,29,31,30,31,30,31,31,30,31,30,31]
    dayOfWeek = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    startDay = 4    # 2016년1월0일 목요일

    # (시작일의 요일 + 해당 월까지의 일의 개수 + 일의 개수) % 요일의 개수
    answer = dayOfWeek[(startDay + sum(num_dayOfMonth[:a-1]) + b) % len(dayOfWeek)]
    return answer
    
if __name__ == "__main__":
    print(solution(5, 24) == "TUE")
    print(solution(1, 1) == "FRI")