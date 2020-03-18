# 1071 : [기초-반복실행구조] 0 입력될 때까지 무한 출력하기1
numList = [int(x) for x in input().split()]
for num in numList:
    if num == 0: break
    print(num)