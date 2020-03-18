# 1045 : [기초-산술연산] 정수 2개 입력받아 자동 계산하기
import decimal
context = decimal.getcontext()
context.rounding = decimal.ROUND_HALF_UP
a,b = [ int(x) for x in input().split() ]
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(round(decimal.Decimal(a/b), 2))