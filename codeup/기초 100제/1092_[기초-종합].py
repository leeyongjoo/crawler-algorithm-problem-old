# 1092 : [기초-종합] 함께 문제 푸는 날
a, b, c = [int(x) for x in input().split()]
day = 1
while True:
    if day % c == 0 and day % b == 0 and day % a == 0: break
    day += 1
print(day)