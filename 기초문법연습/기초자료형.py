# 숫자형 = int, float, complex

# 시퀀스 = 여러 개의 값들을 순서대로 나열하여 저장하는 자료형 list, tuple, range
# 특징 : 순서대로 저장, 고유 인덱스 존재, 슬라이싱으로 원하는 범위만 추출 등

# 문자열 : 변경불가능한 시퀀스 자료형
# \n 줄바꿈 \t 탭 \\ 백슬래시(2번써야함)

# f-string
name = '희수'
age = 29
print(f'이름은 {name}이고, 나이는 {age}이다.')
print(f'내년 나이는 {age+1} 이다.')

#문자열은 인덱스 사용 불가. s = 'hello , s[0] = 오류발생
s = 'hello'
s= 'H' + s[1:] # 새 문자열 생성
print(s)

#리스트 : 여러개의 값을 순서대로 저장하는 변경 가능 시퀀스 자료형
fruits = ['apple', 'banana', 'cherry']
mix = [1, 'hello', 3.141592, True] # 데이터 타입 상관없음

print(fruits[0])
print(fruits[-1])
print(fruits[0:2])

mat = [[1,2,3],[4,5,6]]
print(mat[1][2])

# 튜플 : 여러 개의 값을 순서대로 저장하는 변경 불가능한 시퀀스
t1 = (1,2,3)
t2 = 1,2,3 #괄호 생략가능
t3 = (42,) # 하나도 가능하지만 마지막 쉼표 필수!
# t3 = (42) 이건 그냥 int

# 튜플 사용예시
x,y = 10, 20 #다중 할당
x,y = y,x # 값 교환
def min_max(nums): 
    return min(nums), max(nums)

lo, hi = min_max([3,1,4,1,5]) #다중 값 반환
print(lo)
print(hi)

# 딕셔너리 : key - value 쌍으로 이뤄진 **순서없고, 중복없는, 변경가능**한 자료형
person = {'name' : '서희수','age':29, 'lang':'Python'}
#KEY는 중복이 안되며, 값은 중복되어도 된다.
#또한 key는 int, tuple, str같이 변경불가능한 타입만 가능하다.
print(person['name'])
person['e-mail'] = 'heesu710@naver.com' # 값 추가
person['age'] = 30 # 값 변경

# 세트 : 순서와 중복이 없는 변경가능한 자료형
set = {1,2,3,2,1}
print(set) #중복 자동제거

# set, dict - 순서 없음. 변경은 가능

#형 변환
print(3+1.5) #int > float 형 변환
print(1+True) # bool > int 형 변환

print([1,2] + [3,4]) #이어붙이기
print('hi'*3) # 반복
print([0]*5)
