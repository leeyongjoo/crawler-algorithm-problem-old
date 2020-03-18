# 1015 : [기초-입출력] 실수 입력받아 둘째 자리까지 출력하기
import decimal
context = decimal.getcontext()
context.rounding = decimal.ROUND_HALF_UP
print(round(decimal.Decimal(float(input())), 2))