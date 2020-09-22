from random import randrange
'''
Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
50명의 승객과 매칭기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오
조건 1 : 승색별 운행소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
조건 2 : 당신은 소요시간 5분에서 15분 사이의 승객만 매칭해야 합니다.
'''
count = 0
for i in range(1, 51):
    time = randrange(5, 50)
    if time <= 15 and time >=5:
        print('[O]',i,'번째 손님  (소요시간 : ',time,'분)')
        count+=1
    else:
        print('[]{0}번째 손님 (소요시간: {1}분)'.format(i, time))

print('총 탑승 승객: {0}'.format(count))
