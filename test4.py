'''
Quiz) 당신의 학교에서는 파이썬 코딩대회를 주최합니다.
참석률을 높이기 위해서 댓글 이벤트를 진행가리로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오.

조건1 : 편의상 댓글은 20명이 작성하였고, 아이디는 1~20 이라고 가정
조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
조건3 : random 모듈의 shuffle과 sample 활용

출력예제
-- 당첨자 발표 --
치킨당첨자 : 1
커피당첨자 : [2,3,4]
-- 축하합니다 --
'''

from random import *
# id = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
id = range(1, 21) # 1 부터 20까지 숫자 생성
id = list(id) # 타입이 range이기 때문에 리스트로 변환해줌
shuffle(id)
winner = sample(id, 4)
print( '-- 당첨자 발표 --')
print('치킨 당첨자 : {0}'.format(winner[0]))
print('커피 당첨자 : {0}'.format(winner[1:]))
print('-- 축하합니다 --')