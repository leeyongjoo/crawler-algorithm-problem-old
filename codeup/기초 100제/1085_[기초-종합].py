# 1085 : [기초-종합] 소리 파일 저장용량 계산하기
h, b, c, s = [int(x) for x in input().split()]
cap = h * b * c * s / 8 # 1Byte = 8Bits
capUnit = ['', 'K', 'M', 'G', 'T']
capUnitIdx = 0
lenCapUnit = len(capUnit)
while capUnitIdx < 2: # True
    if capUnitIdx == lenCapUnit-1: break
    # if cap < 2**10: break
    cap /= 2**10
    capUnitIdx += 1
print('%.1f %cB' % (cap, capUnit[capUnitIdx]))