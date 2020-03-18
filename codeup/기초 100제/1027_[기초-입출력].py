# 1027 : [기초-입출력] 년월일 입력 받아 형식 바꿔 출력하기
yyyy, mm, dd = input().split('.')
print('{:0>2}-{:0>2}-{:0>4}'.format(dd, mm, yyyy))