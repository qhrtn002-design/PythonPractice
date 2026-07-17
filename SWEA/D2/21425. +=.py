num = int(input())

for _ in range(1,num+1):
    a,b,n = map(int,input().split()) #텍스트 받기

    cnt = 0 #카운팅 지정
    while a <= n and b <= n: # 둘중 하나만 초과되도 종료
        if a < b: # a가 작다면 a에 b더하기
            a+=b
            cnt +=1
        else: # b가 작다면 b에 a 더하기
            b+=a
            cnt +=1
    print(cnt)