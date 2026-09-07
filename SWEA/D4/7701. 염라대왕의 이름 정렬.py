t=int(input())
for s in range(t):
    n=int(input())
    lst=[]
    for _ in range(n):
        text=input()
        lst.append(text)
    lst=list(set(lst))
    lst.sort(key=lambda x:(len(x),x))
    print(f'#{s+1}')
    for i in lst:
        print(i)