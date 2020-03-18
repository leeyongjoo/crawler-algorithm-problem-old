# 1019 : [기초-입출력] 연월일 입력받아 그대로 출력하기
yyyy, mm, dd = input().split('.')
print('{:0>4}.{:0>2}.{:0>2}'.format(yyyy, mm, dd))