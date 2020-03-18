# 1093 : [기초-1차원배열] 이상한 출석 번호 부르기1
# n, *num = [int(x) for x in input().split()]
n = int(input())
numList = [int(x) for x in input().split()]
maxNum = 23
numDict = {a:0 for a in range(1,maxNum+1)}
for a in numList:
    numDict[a] += 1
for i in range(1,maxNum+1):
    print(numDict[i], end=' ')