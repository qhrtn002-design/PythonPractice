t = int(input())

for s in range(1,t+1):
    a = input()
    b = input()

    ans = 0 #최댓값지정은 2중 for문 밖에 지정
    
    for i in a: 
        cnt = 0 #카운팅 값은 글자마다 바뀌므로 글자 바꾸는 곳 바깥인 여기
        for j in range(len(b)):
            if i == b[j]:
                cnt += 1
        if cnt > ans: #최댓값 구하기
            ans = cnt

    print(f'#{s} {ans}')