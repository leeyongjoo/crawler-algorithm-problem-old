# 1065 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기
a = [int(x) for x in input().split() if int(x)%2==0]
for num in a: print(num)