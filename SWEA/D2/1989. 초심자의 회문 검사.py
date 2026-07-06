a = int(input())

for i in range(1,a+1):
    text = list(map(str,input()))
    if text == text[::-1]:
        print(f'#{i} 1')
    else:
        print(f'#{i} 0')