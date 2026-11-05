"""
    1. 첫 번째 줄에는 과목 개수 N(<=1000)
    2. 현재 성적(<=100 & >= 0, 적어도 1개는 0보다 큼)
    3. new 평균식: 과목총합*100/max(성적)/N
"""

n = int(input())
mylist = list(map(int, input().split()))
mymax=max(mylist)
sum=sum(mylist)

print(sum*100/mymax/n)
