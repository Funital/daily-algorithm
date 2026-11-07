"""
    1. 첫 번째 줄에 N과 M.
    2. 두 번째 줄에 N개의 수 A1,...,An
    3. N개의 수가 주어졌을 때, 연속된 부분의 합이 M으로 나누어 떨어지는 구간의 개수 구하기
"""

import sys
input = sys.stdin.readline
n, m = map(int, input().split())    # 첫 번째 줄
A = list(map(int, input().split())) # 두 번째 줄
S = [0] * n # 합 배열
C = [0] * m # 나머지 연산 수행한 합 배열
S[0] = A[0]
answer = 0

for i in range(1, n):
    S[i] = S[i-1] + A[i]    # 합 배열 저장하기

for i in range(n):
    remainder = S[i] % m
    if remainder == 0:
        answer += 1
    C[remainder] += 1   # 나머지가 같은 인덱스의 개수 값 증가시키기

for i in range(m):
    # 나머지가 같은 인덱스 중 2개를 뽑는 경우의 수를 더하기
    if C[i] > 1:
        answer += (C[i] * (C[i]-1) // 2)

print(answer)