t = int(input())
for s in range(1,t+1):
    n = int(input())
    lst = list(map(int, input().split()))

    lst.sort()
    print(f'#{s}',end=' ')
    print(*lst)