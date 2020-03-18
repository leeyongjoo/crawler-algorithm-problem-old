# 1094 : [기초-1차원배열] 이상한 출석 번호 부르기2
# n, *num = [int(x) for x in input().split()]
n = int(input())
numList = [int(x) for x in input().split()]
for a in reversed(numList):
    print(a, end=' ')