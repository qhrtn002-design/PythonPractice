t=int(input())
for tc in range(t):
    n, word = input().split() # 길이와 문자 입력받기
    n = int(n) # 길이를 정수로 변환
    digits = '0123456789ABCDEF' # 숫자에 따른 인덱스 설정
    ans = '' # 정답 문자열 세팅
    for i in word: # 문자를 하나씩 반복
        num = digits.index(i) # 문자에 있는 한 문자의 인덱스를 숫자로.
        temp = '' # 문자 하나에 대한 비트를 담을 문자열 세팅
        for _ in range(4): # 무조건 한 문자당 4자리라 4만큼 반복
            temp = str(num%2) + temp
            # 숫자를 2로 나눈 나머지를 오른쪽에서 왼쪽으로 붙여나감
            num //= 2 # 계속 2로 나눔
        ans += temp # 최종 정답에 하나씩 붙임

    print(f'#{tc+1} {ans}')