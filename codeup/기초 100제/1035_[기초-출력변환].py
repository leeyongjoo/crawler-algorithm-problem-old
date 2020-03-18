# 1035 : [기초-출력변환] 16진 정수 1개 입력받아 8진수로 출력하기
hexNumStr = input()
print('%o' % (int(hexNumStr, 16)))