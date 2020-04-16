# [2018 KAKAO BLIND RECRUITMENT] [1차] 비밀지도
def solution(n, arr1, arr2):
    arr1_int = [int(str(bin(a))[2:], 10) for a in arr1]
    arr2_int = [int(str(bin(a))[2:], 10) for a in arr2]

    arr1_arr2_str = [str(a1+a2) for a1, a2 in zip(arr1_int, arr2_int)]
    arr1_arr2_str_fill = ['0' * (n - len(a)) + a for a in arr1_arr2_str]

    output = []
    for a in arr1_arr2_str_fill:
        col = []
        for b in a:
            if b == '0':
                col.append(' ')
            else:
                col.append('#')
        output.append(''.join(col))
    return output

# 다른 사람의 풀이
def solution(n, arr1, arr2):
    output = []
    for a1, a2 in zip(arr1,arr2):
        col = str(bin(a1|a2))[2:]
        col = col.rjust(n, '0')
        col = col.replace('0', ' ').replace('1', '#')
        output.append(col)
    return output

if __name__ == "__main__":
    n = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]
    print(solution(n, arr1, arr2))
    print(solution(n, arr1, arr2) == ["#####", "# # #", "### #", "#  ##", "#####"])

    n = 6
    arr1 = [46, 33, 33, 22, 31, 50]
    arr2 = [27, 56, 19, 14, 14, 10]
    print(solution(n, arr1, arr2))
    print(solution(n, arr1, arr2) == ["######", "###  #", "##  ##", " #### ", " #####", "### # "])
