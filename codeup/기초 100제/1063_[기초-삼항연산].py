# 1063 : [기초-삼항연산] 두 정수 입력받아 큰 수 출력하기
a,b = [int(x) for x in input().split()]
print(a if a > b else b)