# 1087 : [기초-종합] 여기까지! 이제 그만~
x = int(input())
sum = 0
start = 1
while sum < x:
    sum += start
    start += 1
print(sum)