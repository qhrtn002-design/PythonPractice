a = int(input())

for i in range(1,a+1):
    ans = 0
    str1 = input()
    str2 = input()

    for x in str1:
        cnt = 0
        for y in str2:
            if x == y:
                cnt += 1
        if ans < cnt:
            ans = cnt
    
    print(f'#{a} {ans}')
    