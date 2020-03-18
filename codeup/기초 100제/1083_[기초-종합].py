# 1083 : [기초-종합] 3 6 9 게임의 왕이 되자!
x = int(input())
for i in range(1,x+1):
    if i % 3 == 0: print('X', end=' ')
    else: print(i, end=' ')