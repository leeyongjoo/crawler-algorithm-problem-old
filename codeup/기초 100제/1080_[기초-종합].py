# 1080 : [기초-종합] 언제까지 더해야 할까
x = int(input())
sumToX = 0
for i in range(1,x):
    if sumToX >= x:
        print(i-1)
        break
    sumToX += i