# 1099 : [기초-2차원배열] 성실한 개미
gridList = []   # 격자판
for tmp in range(10):
    gridList.append(list(int(x) for x in input().split()))
startX, startY = 2, 2
startX -= 1
startY -= 1
while True:
    if gridList[startX][startY] == 2:
        gridList[startX][startY] = 9
        break
    gridList[startX][startY] = 9
    if gridList[startX][startY+1] in (0,2):
        startY += 1
    elif gridList[startX+1][startY] in (0,2):
        startX += 1
    else: break
for a in gridList:
    for b in a:
        print(b, end=' ')
    print()