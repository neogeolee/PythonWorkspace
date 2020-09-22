absent = [2, 5] # 결석
no_book = [7] # 책 안들고 왔음
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print('오늘 수업여기까지 {0} 개새끼야 따라와'.format(student))
        break
    print('{0}, 책읽어라'.format(student))