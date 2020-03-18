# 1084 : [기초-종합] 빛 섞어 색 만들기
a,b,c = [int(x) for x in input().split()]
count = 0
for i in range(a):
    for j in range(b):
        for k in range(c):
            print(i, j, k)
            count += 1
print(count)