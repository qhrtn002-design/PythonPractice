t = int(input())

for s in range(1,t+1):
    txt = input()
    lst = []
    for i in txt:
        if len(lst) != 0:
            
            if i == lst[-1]:
                lst.pop()
            else:
                lst.append(i)
        else:
            lst.append(i)

            
    print(f'#{s} {len(lst)}')