t = int(input())
ans = {'p':'q','d':'b','q':'p','b':'d'}
for s in range(1,t+1):
    n = input()
    lst = []
    for i in n:
        lst.append(ans.get(i))
    answer = lst[::-1]
    print(f'#{s} ',end='')
    print(''.join(answer))
