def add(a,b):
    return a + b

a = 3
b = 4
c = add(a,b) # add라는 함수를 지정하지 않으면 오류발생
print(c)

def say(): #입력값이 없어도 작동하는 함수
    return 'HI'
a = say() # 리턴받을 변수 = 함수 이름()
print(a)

def addmany(*args): # 매개변수 이름 앞에 *을 붙이면 입력값을 전부 모아 튜플로 만듦.
    # **을 붙이면 딕셔너리로 만든다.
    result = 0
    for i in args:
        result += i
    return result

result = addmany(1,2,3,4,5,6,7,8,9,10)
print(result)

