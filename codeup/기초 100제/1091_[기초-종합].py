# 1091 : [기초-종합] 수 나열하기3
a, m, d, n = [int(x) for x in input().split()]
answer = a
for i in range(n-1):
    answer = answer*m + d
print(answer)