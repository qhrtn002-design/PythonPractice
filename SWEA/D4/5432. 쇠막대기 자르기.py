t = int(input())
for s in range(t):
    piece, ans = 0,0
    pipe = input()
    for i in range(len(pipe)):
        if pipe[i] == '(':
            piece += 1
        if pipe[i] == ')':
            piece -= 1
            ans += piece if pipe[i-1] == '(' else 1
    print(f'#{s+1} {ans}')