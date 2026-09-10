t=int(input())
for s in range(t):
    n,m=map(int,input().split())
    text=input()
    for i in range(n+m-1):
        word=text[i:i+m]
        if len(word)==m and word == word[::-1]:
            ans=word
            break
        else:
            ans='NONE'
    print(f'#{s+1} {ans}')