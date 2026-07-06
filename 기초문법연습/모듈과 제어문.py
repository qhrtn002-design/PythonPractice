#모듈 : 함수, 변수, 클래스 등을 모은 하나의 .py파일
# import로 불러와서 기능사용

import math #모듈 전체 > 사용 시 math.sqrt(16)로 명시 필요
print(math.pi)
print(math.sqrt(256))

#특정 기능만 : from math import sqrt, pi
#다 가져오기 : from math import * > 사용 시 그냥 sqrt(16)
# 오히려 이름 출동 위험이 있어 권장하지 않음

#파이썬 표준 라이브러리. 별도 설치 없이 import만으로 사용가능
import random
print(random.randint(1,6))

import datetime
print(datetime.date.today())

#제어문: 조건문(if, elif, else)/반복문(for, while)/반복제어(break, continue,pass)
#enumerate : 반복 시 인덱스와 값을 함께 꺼냄

fruits = ["apple", "banana", "cherry"]
for i , j in enumerate(fruits,start=10): #시작인덱스 지정가능
    print(i,j)

