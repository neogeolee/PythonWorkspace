python = "Python is Amazing"
print(python.lower()) # 모든문자 소문자
print(python.upper()) # 모든문자 대문자
print(python[0].isupper()) # 0번째(첫번째) 문자가 대문자냐?
print(len(python)) # 문자열 길이
print(python.replace("Python", "Java")) # "Python" 을 "Java" 로

index = python.index("n") # n 찾기
print(index)
index = python.index("n", index+1) # 두 번째 n 찾기
print(index)
print(python.find("n"))
print(python.find("Java")) # 찾는글자가 없으면 -1로 반환
#print(python.index("Java")) # Java가 없어서 오류처리

print(python.count("n")) # n이 몇개인지

print("나는 %d 살입니다." % 20) # %d 는 정수
print("나는 %s을 좋아합니다." % "파이썬") # %s 는 문자열
print("Apple은 %c로 시작해요" % "A") # %c 는 문자
print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))

print("나는 {}살 입니다.".format(20))
print("나느 {}색과 {}색을 좋아해요".format("파란", "빨간"))
print("나느 {0}색과 {1}색을 좋아해요".format("파란", "빨간"))
print("나느 {1}색과 {0}색을 좋아해요".format("파란", "빨간"))

print("나는 {age}살이며, {color}색을 좋아해요".format(age=20, color="빨간"))