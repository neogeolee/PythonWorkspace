cabinet = {3: '유재석', 100: '김태호'} # key , value 임
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5]) 오류
print(cabinet.get(5))

print(cabinet.get(5, '사용가능'))

print(3 in cabinet)

cabinet = {'A-3':'유재석', 'B-100':'김태호'}
print(cabinet['A-3'])

# 새손님
cabinet['A-3'] = '김종국'
cabinet['C-20'] = '조세호'
print(cabinet)

# 손님이 감
del cabinet['A-3']
print(cabinet)

# key들만 출력
print(cabinet.keys())
# value 들만 출력
print(cabinet.values())
# 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)