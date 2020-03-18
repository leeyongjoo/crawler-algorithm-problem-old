# 1048 : [기초-비트시프트연산] 한 번에 2의 거듭제곱 배로 출력하기
a, b  = [ int(x) for x in input().split() ]
print(a * (2**b))