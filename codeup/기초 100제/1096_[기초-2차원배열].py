# 1096 : [기초-2차원배열] 바둑판에 흰 돌 놓기
n = int(input())
coordinateList = []
for tmp in range(n):
    coordinateList.append(tuple(int(x) for x in input().split()))
width, height = 19, 19
for i in range(1, width+1):
    for j in range(1, height+1):
        if (i, j) in coordinateList:
            print(1, end=' ')
        else: print(0, end=' ')
    print()