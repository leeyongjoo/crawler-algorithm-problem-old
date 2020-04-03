# [해시] 전화번호 목록
def solution(phone_book):
    sorted_phone_book = sorted(phone_book, key=len)
    for i, p1 in enumerate(sorted_phone_book):
        for p2 in sorted_phone_book[i + 1:]:
            if p1 == p2[:len(p1)]:
                return False
    return True

if __name__ == "__main__":
    print(solution(["119", "97674223", "1195524421"]) == False)
    print(solution(["123", "456", "789"]) == True)
    print(solution(["12", "123", "1235", "567", "88"]) == False)