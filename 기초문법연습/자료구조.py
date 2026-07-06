#자료주고 : 파이썬은 타입마다 그 데이터를 다루는 메서드를 사용
# 메서드 : 특정 데이터 타입에 속한 함수.

numbers=[3,1,2]
numbers.sort()
print(numbers)

text = 'hello'
print(text.upper())

#공통 시퀀스 메서드 : str, list, tuple, range가 공통으로 가지는 메서드
nums = [10,20,30,20]
print(nums.index(20))
print(nums.count(20))

s = 'banana'
print(s.index('a'))
print(s.count('a'))

#불변 시퀀스 메서드 (문자열 전용) : 문자열은 변경이 불가능해서 새 문자열로 반환
#find, index, startwith, endswith, count
text = 'hello world'
print(text.find('o'))
print(text.find('z')) #못 찾으면 -1 출력, index는 못찾으면 오류난다.

#문자열 조작
text = "  Hello, World  "

print(text.strip()) #양쪽 공백제거
print(text.strip().replace(',','!')) #공백제거 후 문자교체
# split(s) : s기준으로 분리, .title():단어 첫 글자 대문자
# .join(iter) : iter이어붙임

# 가변 시퀀드 메서드(리스트 전용) : 메서드가 원본을 수정
# append 끝에 하나추가, extend 끝에 여러개 추가
# insert(i,x) i위치에 x 삽입 ,remove,pop,clear


lst = [1,2,3]
print(lst.append(4))
print(lst.extend([5,6])) #append, extend는 원본을 수정하기때문에, 
#문자열 처럼 새걸 반환하지 않아 none이 나옴

lst = [1,2,3]
lst.append(4)
lst.extend([5,6])
print(lst)

a = [1,2] 
a.append([3,4])
b = [1,2]
b.extend([3,4]) #append는 통째로 하나로 넣고, extend는 풀어서 넣는다
print(a)
print(b)

nums=[1,2,3,4,5,6]
nums.sort() #정렬
nums.sort(reverse=1) #내림차순으로 정렬
nums.reverse() #아예 뒤집기

original = [3,1,2]
result = sorted(original) #원본은 냅두기
# .sort()은 none을 반환. 만약 x=nums.sort()하면 x는 none이 된다. 
# 원본을 건드리기 때문


#얕은 복사 : 바깥 객체는 새로 만들지만 내부는 여전히 공유
a= [[1,2],[3,4]]
b = a[:]

b.append([5,6])
print(a) # b에 더했어도 a는 변화 없음

b[0][0] = 99 #그러나 내부 요소 수정 시 a도 변경
print(a)

#깊은 복사 : 내부 중첩 객체까지 전부 새로 복사. 원본과 완전분리
import copy
a= [[1,2],[3,4]]
b= copy.deepcopy(a)

b[0][0] = 100
print(a)
print(b)

#문자유형 판별 메서드 (전부 T/F로 반환)
#.isalpha(), .isdigit(), .isspace() :공백, .isupper(), .islower()
