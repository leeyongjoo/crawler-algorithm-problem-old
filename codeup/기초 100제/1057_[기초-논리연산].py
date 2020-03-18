# 1057 : [기초-논리연산] 참/거짓이 서로 같을 때에만 참 출력하기
print(sum([int(x) for x in input().split()] + [1]) %2)