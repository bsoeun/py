#과제11
# a = list(map(int, input("숫자 5개 입력:").split()))
# b = map(int, input("숫자 5개 입력:").split())
# a.extend(b)
# print(a)

# a = list(map(int, input("숫자 5개 입력:").split()))
# b = map(int, input("숫자 5개 입력:").split())
# a.append(b)
# print(a)          #오류 map이 있어서 인 것 같음 왜 그런건지?

#과제12
# a = list(map(int, input("숫자 5개 입력:").split()))
# a.pop()
# a.pop()
# print(a)

#과제13
# a = list(map(int, input("숫자 5개 입력:").split()))

# for index, value in enumerate(a):
#     # print(101. value,)????
    
#과제 14
# a =[10, 20, 30, 40, 30, 20, 10]
# print(a.count(20))

#과제15
# a = list(map(int, input("숫자 10개 입력:").split()))
# smallest =a[0]
# largest =a[0]

# for i in a:
#     if i < smallest:
#         smallest = i
# for i in a:
#     if i > largest:
#         largest = i

# print(smallest,largest)

#과제16
# a = list(map(int, input("숫자 10개 입력:").split()))
# b= sum(a)-min(a)-max(a)
# print(b)

#과제17
# a = [10, 20, 30, 40, 30, 20, 10]
# b = a.count(20)
# for i in range(b):
#     a.remove(20)
# print(a)

#과제18
# a = [i for i in range(1, 6)]
# print(a)

#과제19
# a = [i for i in range(1, 20) if i%2==0]
# print(a)

#과제20
# a, b = map(int, input().split())
# c = [2 ** i for i in range(a, b + 1)]
# del c[1]
# del c[-2]
# print(c)

#21
# text = input()
# print(text.replace('Hello', 'Hi'))

#22
# chars = input().split()
# print('/'.join(chars))

#23
# last_name = input()  # 예: KIM
# print(last_name.lower().rjust(10))

#24
prices = input().split(';')

prices = sorted([int(p) for p in prices], reverse=True)

for price in prices:
    print(str(price).rjust(9))