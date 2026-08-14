t = int(input())
for s in range(t):
    n = int(input())
    lst=list(map(int, input().split()))
    ans='Yes' if len(set(lst))==n else 'No'
    print(f'#{s+1} {ans}')