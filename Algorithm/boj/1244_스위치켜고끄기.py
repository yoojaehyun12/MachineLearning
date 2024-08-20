# https://www.acmicpc.net/problem/1244


# 스위치 개수
N = int(input())
# 초기 스위치 [0,1,0,1,0,0,0,1]
switches = list(map(int, input().split()))

student_cnt = int(input())

for _ in range(student_cnt):
    gender, no = map(int, input().split())

    # 남학생일 때
    if gender == 1:
        # no의 배수들을 모두 바꾼다
        pass
    # 여학생일 때
    else:
        # no를 바꾸고, 좌우 대칭일경우 하나씩 늘어나며 바꾼다.
        # 단 대칭이 아니거나, 0 <= idx < N 일 경우 그만둔다.
        pass



print(' '.join(map(str, switches)))






# 8
# 0 1 0 1 0 0 0 1
# 2
# 1 3
# 2 3


# switch = int(input())
# switch_state = list()
# tmp = input().split()
#
# for i in range(0, switch):
#     switch_state.append(int(tmp[i]))
# student = int(input())
#
# for i in range(0, student):
#     tmp = input().split()
#     student_gender = int(tmp[0])
#     student_value = int(tmp[1])
#     value_tmp = student_value
#
#     if student_gender == 1:
#         while student_value <= switch:
#             switch_state[student_value - 1] = 1 - switch_state[student_value - 1]
#             student_value = student_value + value_tmp
#     elif student_gender == 2:
#         switch_state[student_value - 1] = 1 - switch_state[student_value - 1]
#         left = student_value - 1
#         right = student_value + 1
#
#
#         while left > 0 and right <= switch:
#             if switch_state[left - 1] != switch_state[right - 1]:
#                 break
#             switch_state[left - 1] = 1 - switch_state[left - 1]
#             switch_state[right - 1] = 1 - switch_state[right - 1]
#             right = right + 1
#             left = left - 1
# count = 0
#
# for i in range(0, switch):
#     if count < 19:
#         print(switch_state[i], end=' ')
#         count = count + 1
#     else:
#         print(switch_state[i])
#         count = 0




