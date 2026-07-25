t = int(input())
for s in range(1,t+1):
    n = input()
    cnt = 0 #하나만 만족해도 되는경우, 초기값 0
    ans = 'No'
    if len(set(n)) == 2: #세트로 만들어서 4글자가 2글자인경우,
        ans = 'Yes' #답은 yes가 된다.
        for i in n:
            for j in n:
                if i == j:
                    cnt += 1 #문자열내에 같은 글자가 2개씩인지 확인
            if cnt == 2: 
                ans = 'Yes'
                break
    
    print(f'#{s} {ans}')