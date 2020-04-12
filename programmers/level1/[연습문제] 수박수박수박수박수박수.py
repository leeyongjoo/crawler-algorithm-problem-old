# [연습문제] 수박수박수박수박수박수
def solution(n):
    word = '수박'
    word_len = len(word)
    return ''.join([word[i%word_len] for i in range(n)])
    
if __name__ == "__main__":
    print(solution(3) == "수박수")
    print(solution(4) == "수박수박")