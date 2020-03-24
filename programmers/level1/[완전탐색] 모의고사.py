# [완전탐색] 모의고사
def solution(answers):
    random_answer_list = []
    random_answer_list.append((1, 2, 3, 4, 5))
    random_answer_list.append((2, 1, 2, 3, 2, 4, 2, 5))
    random_answer_list.append((3, 3, 1, 1, 2, 2, 4, 4, 5, 5))

    collect_answer_list = [0 for _ in random_answer_list]
    for i, a in enumerate(answers):
        for j, ra in enumerate(random_answer_list):
            if ra[i%len(random_answer_list[j])] == a:
                collect_answer_list[j] += 1

    max_collect_num = max(collect_answer_list)
    answer = [i+1 for i, ca in enumerate(collect_answer_list) if ca == max_collect_num]
    return answer
    
if __name__ == "__main__":
    print(solution([1,2,3,4,5]) == [1])
    print(solution([1,3,2,4,2]) == [1,2,3])