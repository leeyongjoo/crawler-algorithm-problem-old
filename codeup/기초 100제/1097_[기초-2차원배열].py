# 1097 : [기초-2차원배열] 바둑알 십자 뒤집기
width, height = 19, 19
coordinateList = []
for tmp in range(width):
    coordinateList.append(list(int(x) for x in input().split()))
n = int(input())
xyList = []
for tmp in range(n):
    tmpInput = [int(x) for x in input().split()]
    xyList.append(tmpInput)
for xy in xyList:
    x, y = xy
    for i in range(width):
        coordinateList[i][y-1] = (coordinateList[i][y-1] + 1) % 2
    for i in range(height):
        coordinateList[x-1][i] = (coordinateList[x-1][i] + 1) % 2
for i in range(width):
    for j in range(height):
        print(coordinateList[i][j], end=' ')
    print()