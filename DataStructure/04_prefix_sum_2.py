"""
    1. 첫 번째 줄에는 표의 크기 N, 합 구해야 하는 횟수 M
    2. 두 번째 줄부터는 N개의 줄에는 표에 채워져 있는 수가 1행부터 주어짐.
    3. 다음은 M개의 줄. 4개의 정수 X1, Y1, X2, Y2가 주어짐.
    4. 출력은 (X1, Y1)~(X2,Y2)의 합을 구해 출력.
"""

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = [[0] * (n+1)]
D = [[0] * (n+1) for _ in range((n+1))]

for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

for i in range(1, n+1):
    for j in range(1, n+1):
        # 합배열 구하기
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    # 구간 합배열로 질의에 답변
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)