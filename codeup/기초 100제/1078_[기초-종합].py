# 1078 : [기초-종합] 짝수 합 구하기
x = int(input())
evenList = [a for a in range(x+1) if a % 2 == 0]
print(sum(evenList))