t=int(input())
for s in range(t):
    n,m=map(int,input().split())
    text=input()
    for i in range(n-m+1):
        if text[i:i+m] == text[i:i+m][::-1]:
            ans = text[i:i+m]
            break
        else:
            ans='NONE'
    print(f'#{s+1} {ans}')