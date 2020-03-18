# 1088 : [기초-종합] 3의 배수는 통과
x = int(input())
start = 1
prog = start
while prog <= x:
    if prog % 3 == 0: pass
    else: print(prog, end=' ')
    prog += 1