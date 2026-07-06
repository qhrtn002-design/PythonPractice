def greet(name):
    return f'안녕, {name}!' #함수는 return 값을 만나면 즉시 반환하며 종료

message = greet('희수') #함수 호출
print(message) #안녕, 희수!

#여러 값을 반환하면 튜플로 묶어서 반환한다.
def min_max(nums):
    return min(nums), max(nums)

result = min_max([3,1,4])
lo,hi = min_max([3,1,4])
print(result) # 1,4를 튜플로 반환
print(lo, hi) #언패킹으로 분리

def intro(name, age):
    return(f'{name}, {age}세')

print(intro('희수', 29)) #순서대로 값 전달

#기본값을 설정할 수 있다.
def func(name, greeting='HI'):
    print(f'{greeting},{name}')

func('희수') #HI 희수
func('희수','반가워') #반가워 희수

# 기본값이 있는 매개변수가 뒤로 와야한다.
# def f(a=1,b) > 오류발생
# def f(b, a=1):  이렇게 되야함

#가변 인자 : 개수가 정해지지 않은 위치 인자들을 튜플로 받음
def total(*args):
    print(args)
    return sum(args)
print(total(1,2,3,4)) # 개수 자유

#가변 키워드 인자 : 개수가 정해지지 않은 키워드 인자를 딕셔너리로 받음
def info(**kw):
    print(kw)
info(name='희수', age =29)

# 인자 작성 순서는 위치> 기본값> *args> 키워드> **kw 순서대로 작성
#def func(pos, default=0, *args, **kw)

#내장 함수

# len : 길이, abs : 절대값, sorted([3,1,2]) : 정렬

#map : 모든 요소에 함수 적용
nums=[1,2,3]
print(list(map(str,nums))) #요소를 모두 문자로 변경

#filter : 조건 만족하는 요소만
print(list(filter(lambda x:x>1, nums))) #[2,3]

#zips : 여러 시퀀스 짝지음
names = ['a','b']
ages = [25, 30]
print(list(zip(names, ages))) # [('a', 25), ('b', 30)]

#패킹 : 여러 개의 값을 하나로 묶는 것. *을 쓰면 나머지를 리스트로 묶는다.
j, *k = [1,2,3,4]
print(j)
print(k)

first,*middle,last = [1,2,3,4]
print(middle)

#언패킹 : 묶인 값을 풀어서 개별 값으로 나눔
num= [1,2,3]
print(*num) #print(1,2,3)과 동일

#람다 표현식 : 이름없이 한 줄로 함수를 정의
add = lambda a, b : a + b
print(add(3,6)) #주로 일회성 함수로 사용.
# 예시 - list(map(lambda x : x*2, nums))

