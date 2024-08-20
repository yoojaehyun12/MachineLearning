# rewjgrewljgrlekwgjlerjglkgjlerjgerlgjljelk (주석처리하고싶을때 ctrl + /)

def solution(numbers):
    # 0 ~ 9 까지 집합(set())만들기
    # set()은 차집합이 된다.
    all_num = set([0,1,2,3,4,5,6,7,8,9]) - set(numbers)
    return sum(all_num)
    # sum 을 통해 all_num 을 더해서 반환






print(solution([1,2,3,4,6,7,8,0]))  # 14
print(solution([5,8,4,0,6,7,9]))  # 6