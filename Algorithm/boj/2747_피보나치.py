# https://www.acmicpc.net/problem/2747

    # 반복문을 쓴다 언제까지? 총합이 55가 될때까지



n = int(input())

fib = [0, 1]
 # 2
# fib.append(fib[0] + fib[1]) # [0, 1, 1]
#
#   # 3
# fib.append(fib[1] + fib[2]) # [0, 1, 1, 2]
#
#   # 4
# fib.append(fib[2] + fib[3]) # [0, 1, 1, 2, 3]
#
#  # 5
# fib.append(fib[3] + fib[4]) # [0, 1, 1, 2, 3, 5]

for i in range(2,n+1):
    fib.append(fib[i-2] + fib[i-1])

print(fib[n])






