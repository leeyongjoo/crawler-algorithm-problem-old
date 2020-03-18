# 1066 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝/홀 출력하기
numList = [int(x) for x in input().split()]
for num in numList:
    if num % 2 == 0: print('even')
    else: print('odd')