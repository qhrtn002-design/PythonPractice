t=int(input())
for s in range(t):
    n=input()
    lst = []
    ans = 1
    for i in n:
        if i == '(' or i == '{':
            lst.append(i)
        elif i==')'or i=='}':
            if len(lst) == 0:
                ans = 0
            elif i=='}' and lst[-1] == '{':
                lst.pop()
            elif i==")" and lst[-1] == '(':
                lst.pop()
            else:
                ans = 0
    if len(lst)!=0:
        ans=0
    print(f'#{s+1} {ans}')