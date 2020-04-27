# [스택큐] 주식가격
def solution(prices):
    count_sec = [0] * len(prices)
    for i, p1 in enumerate(prices):
        for p2 in prices[i+1:]:
            count_sec[i] += 1
            if p1 > p2:
                break
    return count_sec

# 다른 풀이(효율성 통과)
def solution(prices):
    num_prices = len(prices)
    count_sec = [0] * num_prices
    stack = []
    for i, p in enumerate(prices):
        while stack and prices[stack[-1]] > p:
            idx = stack.pop()
            count_sec[idx] = i - idx
        else:
            stack.append(i)
    while stack:
        idx = stack.pop()
        count_sec[idx] = num_prices - 1 - idx
    return count_sec

if __name__ == "__main__":
    print(solution([1, 2, 3, 2, 3]))
    print(solution([1, 2, 3, 2, 3]) == [4, 3, 1, 1, 0])
