def swap(cnt):
    global ans
    if cnt == n:
        ans = max(ans, int(''.join(num)))
        return
    for i in range(len(num)-1):
        for j in range(i+1, len(num)):
            num[i], num[j] = num[j], num[i]
            if ''.join(num) not in memo[cnt+1]:
                memo[cnt+1].add(''.join(num))
                swap(cnt+1)
            num[i], num[j] = num[j], num[i]

t=int(input())
for s in range(t):
    ans = 0
    num,n = input().split()
    num = list(num)
    n=int(n)
    memo = [set() for _ in range(n+1)]
    swap(0)
    print(f'#{s+1} {ans}')