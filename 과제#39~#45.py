#39 사용자로부터 양수(숫자)를 입력받아서, 0부터 해당 숫자포함까지 홀수를 출력. 단 user-defined function를 이용
# def print_odds(limit):
#     for i in range(limit + 1):
#         if i % 2 != 0:
#             print(i)

# a = int(input("양수를 입력하세요: "))
# print_odds(a)

#40 사용자로부터 숫자를 입력받아서 3의 배수일때만 출력. 단 user-defined function를 이용
# def print_three(n):
#     if n % 3 == 0:
#         print(n)
#     else:
#         print("3의 배수가 아닙니다.")

# num = int(input("숫자를 입력하세요: "))
# print_three(num)

#41 사용자로부터 숫자 4개를 입력받은 후, 최댓값과 최솟값을 계산. 단 user-defined function를 이용하고 함수의 매개변수는
#점수 4개를 받고, 최댓값과 최솟값을 리턴

# def find_max_min(a, b, c, d):
#     numbers = [a, b, c, d]
#     maximum = max(numbers)
#     minimum = min(numbers) 
#     return maximum, minimum

# n1 = int(input("첫 번째 숫자 입력: "))
# n2 = int(input("두 번째 숫자 입력: "))
# n3 = int(input("세 번째 숫자 입력: "))
# n4 = int(input("네 번째 숫자 입력: "))

# max_val, min_val = find_max_min(n1, n2, n3, n4)
# print("최댓값:", max_val)
# print("최솟값:", min_val)

#42 39번이랑 문제 중복이어서 안하겠습니다.
#43 사용자로부터 0보다 크거나 같은 정수 n을 입력받아 n! (펙토리얼)을 계산해서 출력. 단 user-defined function를 이용

# def factorial(n):
#     x = 1
#     for i in range(1, n + 1):
#         x *= i
#     return x

# num = int(input("0 이상의 정수를 입력하세요: "))

# if num >= 0:
#     print(f"{num}! = {factorial(num)}")
# else:
#     print("0 이상의 정수를 입력해야 합니다.")

#44 사용자로부터 2이상 9이하의 양수(숫자) 2개(i, j)를 입력받아서, 이중반복문을 돌면서 i와 j의 곱이 30 이상인 경우의 총 합을 출력. 단 user-defined function를 이용
# def sum_over_30(i, j):
#     total = 0
#     for x in range(1, i + 1):
#         for y in range(1, j + 1):
#             if x * y >= 30:
#                 total += x * y
#     return total

# i = int(input("2 이상 9 이하의 첫 번째 숫자 i를 입력하세요: "))
# j = int(input("2 이상 9 이하의 두 번째 숫자 j를 입력하세요: "))

# if 2 <= i <= 9 and 2 <= j <= 9:
#     result = sum_over_30(i, j)
#     print("총 합:",result)
# else:
#     print("입력값은 2 이상 9 이하의 양수여야 합니다.")

#45) a = [1, 2, 3, 4, 5] 리스트를 함수의 입력으로 받아서 리스트 값의 누적 합을 출력. 단 user-defined function를 이용
def list_sum(lst):
    total = 0
    for value in lst:
        total += value
    return total

a = list(map(int, input("숫자 입력(공백으로 구분): ").split()))
print("입력된 리스트:", a)
print("리스트 합계:", list_sum(a))