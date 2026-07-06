# 2번 1부터 1000까지 3의 배수 합 출력
result = 0 
i = 1
while i <= 1000:
    if i%3 == 0:
        result +=i #result에 i 더하기
    i += 1 #i 는 다시 1씩 증가
print(result)

# 3번 별 표시하기
i = 0
while True:
    i += 1
    if i>5: break
    print('*'*i)

# 4번 1부터 100까지 출력
for i in range(101):
    print(i)

# 5번 평균 구하기
A = [70,60,55,75,95,90,80,80,85,100]
total = 0
for score in A:
    total += score
average = total / len(A)
print(average)

# 6번 리스트 컴프리헨션 사용
num = [1,2,3,4,5]
result = [i*2 for i in num if i%2 == 1]
print(result)
