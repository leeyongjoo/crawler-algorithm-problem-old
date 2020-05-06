# [완전탐색] 소수 찾기
def solution(numbers):
    from itertools import permutations
    num_set = set(int(a) for a in set(numbers))
    for i in range(2, len(numbers)+1):
        num_set.update([int(''.join(a)) for a in set(permutations(numbers, i))])

    sorted_num_list = list(num_set)
    sorted_num_list.sort()
    n = sorted_num_list[-1]
    prime_arr = [False, False] + [True] * (n - 1)
    for i in range(2, n + 1):
        if prime_arr[i]:
            for j in range(i * 2, n + 1, i):
                prime_arr[j] = False
    return len([a for a in sorted_num_list if prime_arr[a]])

if __name__ == "__main__":
    print(solution("17"))
    print(solution("17") == 3)
    print(solution("011"))
    print(solution("011") == 2)