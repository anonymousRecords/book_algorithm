# 1부터 n까지 연속한 숫자의 합을 구하는 알고리즘 1
# 입력 : n
# 출력 : 1부터 n까지의 숫자를 더한 값

from re import s


def sum_n(n):
    s = 0 # 합을 계산할 변수
    for i in range(1, n + 1): # 1부터 n까지 반복(n+1은 제외)
        s = s + i
    return s
print(sum_n(10)) # 1부터 10까지의 합 (입력 : 10, 출력 : 55)
print(sum_n(100)) # 1부터 100까지의 합 (입력 : 100, 출력 : 5050)