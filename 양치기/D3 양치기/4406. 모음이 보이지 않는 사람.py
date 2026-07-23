t = int(input())
moeum = ['a','e','i','o','u']

for s in range(1,t+1):
    fin = []
    ans = input()
    for i in ans:
        if i not in moeum:
            fin.append(i)
    print(f'#{s} ',end='')
    print(''.join(str(x) for x in fin))
