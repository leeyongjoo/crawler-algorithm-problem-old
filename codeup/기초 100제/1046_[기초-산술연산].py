# 1046 : [기초-산술연산] 정수 3개 입력받아 합과 평균 출력하기
numList = [ int(x) for x in input().split() ]
print(sum(numList))
print('%.1f' % (sum(numList)/len(numList)))