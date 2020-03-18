# 1025 : [기초-입출력] 정수 1개 입력받아 나누어 출력하기
n = list(input())
while n:
    print('[{0}{1}]'.format(n[0], '0'*(len(n)-1)))
    n.pop(0)