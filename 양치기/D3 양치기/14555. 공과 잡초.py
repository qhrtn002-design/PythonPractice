t = int(input())
for s in range(1, t+1):
    n = input()
    cnt = 0
    ball = 0
    for i in n:
        if i == '(' or i == ')':
            cnt += 1
    for j in range(len(n)):
        if n[j] == '(' and n[j+1] == ')':
            ball += 1

    ans = cnt - ball
    print(f'#{s} {ans}')