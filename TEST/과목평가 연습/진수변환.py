# 2진수 > 16진수
t=int(input())
for tc in range(t):
    n , word = input().split()
    digit = '0123456789ABCDEF'
    ans = 0
    for i in word:
        ans = ans * 2 + digit.index(i)
    result = ''
    if ans == 0:
        result = '0'
    while ans > 0:
        result = digit[ans%16] + result
        ans //= 16

    print(f'#{tc+1} {result}')


# 8진수 > 16진수
t=int(input())
for tc in range(t):
    n , word = input().split()
    digit = '0123456789ABCDEF'
    ans = 0
    for i in word:
        ans = ans * 8 + digit.index(i)
    result = ''
    if ans == 0:
        result = '0'
    while ans > 0:
        result = digit[ans%16] + result
        ans //= 16

    print(f'#{tc+1} {result}')


# 2진수 > 8진수
t=int(input())
for tc in range(t):
    n, word = input().split()
    ans = 0
    digit = '0123456789ABCDEF'
    for i in word:
        ans = ans * 2 + digit.index(i)
    result = ''
    if ans == 0:
        result = '0'
    while ans > 0:
        result = digit[ans%8] + result
        ans //= 8
    print(f'#{tc+1} {result}')

t= int(input())
for tc in range(t):
    a,b,word = input().split()
    a,b = int(a),int(b)
    ans = 0
    digit = '0123456789ABCDEF'
    for i in word:
        ans = ans * a + digit.index(i)
    result = ''
    if ans == 0:
        result = '0'
    while ans > 0:
        result = digit[ans%b] + result
        ans //= b
    print(f'#{tc+1} {result}')