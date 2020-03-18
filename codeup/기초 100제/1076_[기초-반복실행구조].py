# 1076 : [기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기
alphaOrd = ord(input())
startAlphaOrd = ord('a')
while startAlphaOrd <= alphaOrd:
    print(chr(startAlphaOrd))
    startAlphaOrd += 1