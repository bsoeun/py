# for i in range(3):
#     for j in range(3):
#         if i == j:
#             continue
#         if i + j ==3:
#             break
#         print("%d, %d" % (i, j))
#     print('stop\n')

# for num in range(1, 30):
#     if num == 1:
#         continue
    
#     if num >10:
#         break
#     flag = 0

#     for i in range(2, num):
#         if num % i == 0:
#             flag = 1
#             break
#     if flag == 0:
#         print(num)
# print("end")

# a= [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(a[-5:])

# a = [[10, 20],
#      [30, 40],
#      [50, 60]]
# for x in a:
#     print(x)
#     for y in x:
#         print(y, end='')
#     print()

# for x, y in a:
#     print(x,y)

# a = str.maketrans('abcde', "12345")
# print(input(":").translate(a))

# aw = "a s dsd gh"
# c='ad'
# # c=aw.index('s')
# # print(c)
# print('hi, {1} {0}'.format(aw,c))

# a = input(':').split()
# print([a[-1]])
# print(a)

# a = list(map(int, input(':').split()))
# print(a[-1]) #굿

# a =map(int, input(':').split())
# print(a[-1])

# a =[1, 56, 23, 34]

# b = list(a)
# a = a.(90)
# print(b)
# print(a)

# a =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # print(a[:len(a)])
# a[len(a):]=[11]
# print(a)

a = [34, 23, 34, 43, 89]

# for x, y in enumerate(a, start=1):
#     print(y, x)

# i=0
# while i < len(a):
#     print(i, a[i])
#     i+=1

# a = input('')#.split()
# print(a)

print(a.sort())