t = int(input())

for s in range(1,t+1):
    x, y = map(int,input().split())
    a = set(map(int,input().split()))
    b = set(map(int,input().split()))

    if a == b:
        ans = '='
    elif a<b:
        ans = '<'
    elif a>b:
        ans = '>'
    else:
        ans = '?'
    print(ans)