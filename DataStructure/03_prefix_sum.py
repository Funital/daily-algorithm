"""
    1. 첫 번째 줄에 수의 개수 N(1<=N<=100,000)과 합을 구해야하는 횟수 M(1<=M<=100,000)
    2. 두 번째 줄에는 N개의 수
    3. 세 번쨰 줄부터는 M개의 줄에 합 구해야 하는 구간 i와 j
"""

import sys

input = sys.stdin.readline
suNo, quizNo = map(int, input().split())
numbers=list(map(int, input().split()))
prefix_sum=[0]
temp=0

for i in numbers:
    temp = temp+i
    prefix_sum.append(temp)

for i in range(quizNo):
    s,e=map(int, input().split())
    print(prefix_sum[e]-prefix_sum[s-1])