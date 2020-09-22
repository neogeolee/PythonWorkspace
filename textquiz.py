url = "http://naver.com"

# result1 = url[7:]
# print(result1)
result1 = url.replace("http://", "")
# result2 = result1[:5]
result2 = result1[:result1.index(".")] # 위에꺼랑 같음
# print(result2)
result3 = result2[:3] + str(len(result2)) + str(result2.count("e")) + "!"

# print(result3)

print("{0} 의 비밀번호는 {1} 입니다.".format(url, result3))
