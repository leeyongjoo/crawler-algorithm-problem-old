# 1082 : [기초-종합] 16진수 구구단
x = int(input(), 16)
for i in range(1, 16):
    print('%X*%X=%X' % (x,i,x*i))