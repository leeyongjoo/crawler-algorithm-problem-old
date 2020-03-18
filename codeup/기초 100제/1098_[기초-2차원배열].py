# 1098 : [기초-2차원배열] 설탕과자 뽑기
h, w = [int(x) for x in input().split()] # 가로, 세로
n = int(input())    # 막대의 개수
stickList = []  # 길이, 방향, 좌표(x, y)
for tmp in range(n):
    stickList.append(tuple(int(x) for x in input().split()))
gridList = []   # 격자판
for tmp in range(h):
    gridList.append([0 for a in range(w)])
for stick in stickList:
    l, d, x, y = stick
    if d == 0:
        for i in range(l):
            gridList[x-1][y-1+i] = 1
    elif d == 1:
        for i in range(l):
            gridList[x-1+i][y-1] = 1
for a in gridList:
    for b in a:
        print(b, end=' ')
    print()