# 1055 : [기초-논리연산] 하나라도 참이면 참 출력하기
if any([int(x) for x in input().split()]): print(1)
else: print(0)