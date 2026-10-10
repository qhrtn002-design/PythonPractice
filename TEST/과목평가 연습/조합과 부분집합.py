# def dfs(num,idx):
#     if num == m:
#         print(*ans)
#         return
    
#     for i in range(idx,n+1):
#         ans.append(i)
#         dfs(num+1,i+1)
#         ans.pop()

# t=int(input())
# for tc in range(t):
#     n,m = map(int,input().split())
#     ans = []
#     print(f'#{tc+1}')
#     dfs(0,1)


# result = '0' * (width - len(result)) + result

t=int(input())
for tc in range(t):
    digit = '0123456789ABCDEF'
    n, word = input().split()
    ans = 0
    result = ''
    for i in word:
        ans = ans * 16 + digit.index(i)
    if ans == 0:
        result = '0'
    while ans > 0:
        result = digit[ans%2] + result
        ans //= 2
    
    print(f'#{tc+1} {result}')