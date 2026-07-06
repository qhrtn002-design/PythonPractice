test = ['one', 'two', 'three']
for i in test: # test 내용을 차례대로 i 에 대입
    print(i)

marks = [90, 25, 67, 45, 80]
num = 0
for i in marks: # i에 marks 원소 대입
    num +=1
    if i < 60:
        continue

    print("%d번 학생은 합격입니다." % num)

add = 0
for i in range(101):
    add += i
print(add)


for i in range(1,10):
    for j in range(1, 10):
        print(i*j, end=' ')
    print('') # 구구단 1단이 끝날때마다 줄 바꿈
    #print마다 줄바꿈이 자동인 파이썬의 특징을 이용

a = [1,2,3,4]
result = []
for num in a: #리스트 a의 각 원소를 차례대로 num에 대입하며 반복
    result.append(num*3) #리스트의 각 항목에 3을 곱한 값을 result에 삽입
print(result)

#그러나,
result = [num * 3 for num in a] #리스트 컴프리헨션을 사용, 더 간단히 작성가능.
print(result)
result = [num * 3 for num in a if num % 2 == 0] #이렇게 내부에 조건문도 가능
print(result)