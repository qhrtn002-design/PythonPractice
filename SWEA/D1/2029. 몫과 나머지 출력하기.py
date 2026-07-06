n = int(input())
for i in range(1, n+1): #1부터 사용하도록 범위 지정
    a, b = map(int, input().split()) # 숫자 두개 공백 구분해서 int로 받음
    print(f'#{i} {a//b} {a%b}') # f string 사용
