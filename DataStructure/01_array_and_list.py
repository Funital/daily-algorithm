"""
    N개의 숫자가 공백 없이 쓰임. 이 숫자 모두 합해 출력하는 프로그램 작성
    ex) (입력) 5      (출력) 15
              54321
"""

n = input()

numbers = list(input())
total=0

for number in numbers:
    total += int(number)

print(total)
