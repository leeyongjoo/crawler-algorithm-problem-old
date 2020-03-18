# 1070 : [기초-조건/선택실행구조] 월 입력받아 계절 출력하기
mm = int(input())
mm %= 12
if mm < 3: print('winter')
elif mm < 6: print('spring')
elif mm < 9: print('summer')
elif mm < 12: print('fall')