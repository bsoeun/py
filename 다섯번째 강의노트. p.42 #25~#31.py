# dictionary
# lux = {'health':490, 'mana':334, 'melee':550, 'armor':18.72}
# print(lux['health'])
# print(lux)

# lux = {'health':490, 'health':800, 'mana':334, 'melee':550, 'armor':18.72}
# print(lux['health'])
# print(lux)

# x = {100:'hundred', False: 0, 3.5: [3.5, 3.5]}
# print(x) #list, dictionay는 사용불가

# x= {}
# y= dict(키1=값1, 키2=값2) #작은 따옴표, 큰 따옴표 사용X
# y= dict(zip(['키1', '키2'], [값1, 값2]))
# y= dict([('키1', 값1),('키1', 값2)])
# y= dict({'키1':값1, '키1':값2})

#키에 할당
#lux['health'] = 200

#dictionary에 없는 키 가져오라고 하면 에러

#키 확인
#print('healht'in lux) >>> True or False
#print(len(lux))

# x= {'a':10, 'b':20, 'c':30, 'd':40}
# returnvalue1 = x.setdefault('e')
# print(x)
# returnvalue2 = x.setdefault('f', 100)
# print(x)
# print(returnvalue1, returnvalue2)

# x.update(a=99)
# print(x)
# x.update(e=99)
# print(x)

# return_value = x.pop('a')
# del x['a']
# return_value = x.popitem()
# x.clear()
# return_value = x.get('a') #키 없으면 none 값이 없으면?
# x.items() #키와 값
# x.keys() #키
# x.values() #값
# x.copy()

# keys = ['a', 'b', 'c', 'd']
# x = dict.fromkeys(keys, 100)
# print(x)
# for i in x:
#     print(i, end=' ')

# x = {'a': 10, 'b':20, 'c':30, 'd':40}
# for i, j in x.items():
#     print(i, j)
# for i, j in {'a': 10, 'b':20, 'c':30, 'd':40}.items():
#     print(i, j)

# dictionary comprehension
# keys = ['a', 'b', 'c', 'd']
# x = {key: value for key, value in dict.fromkeys(keys).items()}
# print(x)