# 1034 : [기초-출력변환] 8진 정수 1개 입력받아 10진수로 출력하기
octNumStr = '0o' + input()
print('%d' % int(octNumStr, 8))