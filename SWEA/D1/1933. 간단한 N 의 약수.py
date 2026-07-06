n = int(input())

for i in range(1, n+1): #0으로 나눌 수 없으므로 1부터 시작.
    if n%i == 0:
        print(i,end=' ') #나누는 수는 줄바꿈 없이 공백만 두고 출력