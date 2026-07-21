t = int(input())

for s in range(1,t+1):
    lst = input()

    for i in range(1, 11):
        flag = 1

        for j in range(i,len(lst)):
            if lst[j] != lst[j-i]:
                flag = 0
                break
                
        if flag:
            ans = i
            break
    print(f'#{s} {ans}')
