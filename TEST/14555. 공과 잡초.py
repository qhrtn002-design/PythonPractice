t=int(input())
for tc in range(t):
    s = input()
    ans=0
    for i in range(len(s)):
        if s[i]=='(' or s[i]==')':
            ans+=1
        if s[i] == '(' and s[i+1]==')':
            ans-=1
    print(f'#{tc+1} {ans}')