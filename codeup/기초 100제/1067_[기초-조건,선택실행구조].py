# 1067 : [기초-조건/선택실행구조] 정수 1개 입력받아 분석하기
num = int(input())
if num < 0: print('minus')
else: print('plus')
if num % 2 == 0: print('even')
else: print('odd')