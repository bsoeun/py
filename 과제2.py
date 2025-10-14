# a =[38, 21, 53, 62, 19]
# smallest = a[0]
# for i in a:
#     if i < smallest:
#         smallest = i
# print(smallest)

# a =[38, 21, 53, 62, 19]
# largest = a[0]
# for i in a:
#     if i > largest:
#         largest = i
# print(largest)

# a =[38, 21, 53, 62, 19]
# a.sort()
# print(a[0], "and", a[-1])

# a =[38, 21, 53, 62, 19]
# min_value = min(a)
# max_value = max(a)
# print(min_value, "and", max_value)

# a =[38, 21, 53, 62, 19]
# result = 0
# for i in a:
#     result += i
# print(result)

# a =[38, 21, 53, 62, 19]
# result =sum(a)
# print(result)

# a= [i for i in range(10)]
# b= list(i for i in range(10))
# print(a)
# print(b)

# a= [i + 5 for i in range(10)]
# b= list(i for i in range(10))
# print(a)
# print(b)

# a= [i for i in range(10) if i % 2 == 0]
# print(a)


# a= [i + 5 for  i in range(10) if i % 2 == 1]
# print(a)

# print(range(10))
# # i = list(range(10))
# # print(i)
# i =range(10)
# i %= 2
# if i == 0:
#     print(i)

#41
# a= [i * j for  j in range(2, 10)for i in range(1, 10)]
# print(a)

# a= [i * j for j in range(2,10)
#           for i in range(1, 10)]
# print(a)

# a= [1.2, 2.5, 3.7, 4.6]
# a =list(map(int, a))
# print(a)

# a= list(map(str, range(10)))
# print(a)

# a= list(map(int, input().split()))
# print(a)

# a= (38, 21, 53, 62, 19, 53)
# b = a.index(53)
# print(b)

# a= (10, 20, 30, 40, 15, 20, 40)
# b = a.count(20)
# print(b)

# a= (38, 21, 53, 62, 19)
# for i in a:
#     print(i, end=' ')

# a= tuple(i +5 for i in range(10) if i % 2 == 1)
# print(a)

# a= (1.2, 2.5, 3.7, 4.6)
# a= tuple(map(int, a))
# print(a)

# a= (38, 21, 53, 62, 19)
# print(min(a), max(a), sum(a))

# a=[[10, 20], [30, 40],[50, 60]]
# b=[[10, 20],
#    [30, 40],
#    [50, 60]]

# print(a)
# print(b)

# a=[[10, 20],
#    [30, 40],
#    [50, 60]]

# print(a[1][0])
# print(a[0][1])

# a[2][1] = 100
# print(a)

# a=[[10, 20],
#    [30, 40],
#    [50, 60]]

# for x, y in a:
#     print(x, y)

a=[[10, 20],
   [30, 40],
   [50, 60]]

for x in a:
    print(x)
    for y in x:
        print(y, end=' ')
    print()