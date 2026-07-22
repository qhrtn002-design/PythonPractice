t = int(input())

for s in range(1, t+1):
    a = input()

    ans = 1 if (a == a[::-1]) else 0
    
    print(f'#{s} {ans}')