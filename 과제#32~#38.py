# 32 숫자 10개 5개씩 나눠 set만들고, 합집합과 교집합 께산 후 출력
# likenum1 = {6, 9, 32, 57, 13}
# likenum2 = {4, 9, 13, 53, 68}
# a = likenum1 | likenum2
# b = likenum1 & likenum2
# print(a, b)

# 33 숫자 10개 5개씩 나눠 set만들고, 차집합과 대칭차집합 께산 후 출력
# likenum1 = {6, 9, 32, 57, 13}
# likenum2 = {4, 9, 13, 53, 68}
# a = likenum1 - likenum2
# b = likenum1 ^ likenum2
# print(a, b)

# 34 숫자 5개로 세트 만든 후, update mathod 이용 숫자 100 할당 후 출력
# likenum1 = {6, 9, 32, 57, 13}
# likenum1.update( {100} )
# print(likenum1)


# 35 a = {100, 200, 300, 400, 500} 선언 후 {400, 500, 600, 700, 800}set과 intersection_updatemethod, difference_updatemethod alc symmetric_difference_updatemethod을 수행 후 출력
# a = {100, 200, 300, 400, 500}
# a.intersection_update({400, 500, 600, 700, 800})
# print(a)
# a.difference_update({400, 500, 600, 700, 800})
# print(a)
# a.symmetric_difference_update({400, 500, 600, 700, 800})
# print(a)

# 36 a = {100, 200, 300, 400, 500}와 {100, 200, 300, 400, 500} a가 상위집합이면 "상위"를 출력 a가 부분 집합이면 "부분"출력 상ㅇ위집합이 부분집합일 경우에 "동시" 출력
# a = {100, 200, 300, 400, 500}
# if a == {100, 200, 300, 400, 500}:
#     print("동일")
# elif a <= {100, 200, 300, 400, 500}:
#     print("부분")
# else:
#     print("상위")


# 37 숫자 5개 set 만든 후 1000숫자 add mehtod이용해 추가 마지막 값을 삭제 후 출력
# likenum1 = {6, 9, 32, 57, 13}
# likenum1.add(1000)
# likenum1.pop()
# print(likenum1)

# 38 아래 코드 완성해 1부터 100 숫자 중 3과 5의 공배수 set comprehension 이용 세트로 출력
multiples ={x for x in range(1, 100)if x%3==0 and x%5==0}
print(multiples)
