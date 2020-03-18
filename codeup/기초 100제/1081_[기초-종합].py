# 1081 : [기초-종합] 주사위를 2개 던지면
n, m = [int(x) for x in input().split()]
for a in range(1, n+1):
    for b in range(1, m+1):
        print(a, b)