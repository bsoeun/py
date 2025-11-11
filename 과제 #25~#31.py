# 25
# x = list(input('키 입력:').split())
# y = list(input('값 입력:').split())
# print(x)

# z = dict(zip(x, y))
# del z['alpha']
# print(z)

# 26
# park = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
# print(park['english'])
# print(park['science'])
 
# 27
# park = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
# parkkeys = dict.fromkeys(park, 100)
# print(parkkeys)

# 28
# lee = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
# print('english'in lee)
# if 'english' in lee:
#     del lee['english']
# print(lee)

# 29
# lim = dict({'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83})
# print(lim.keys(), lim.values())
# print(lim.items())

# 30
# for i in lim.values():
#     if i >= 90:
#         print(i)

# choi = { 'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83 }
# scores = {subject: score for subject, score in choi.items() if score >= 90}
# print(scores.keys())

# 31

yoo = { 'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83 }

average = sum(yoo.values()) / len(yoo)
print("평균 점수:", average)