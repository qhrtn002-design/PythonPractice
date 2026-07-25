t = int(input())
for s in range(1,t+1):
    n,m = map(int,input().split())
    total = 0
    for i in range(n):
        total += 2**i #n칸까지 불켜질때 그 합계
    ans = 'ON' if m & total == total else 'OFF'
    #비트 계산으로 & 연산시 작은 값 그대로 전부 출력.
    #출력값이 합계와 동일하면 정답 출력
    print(f'#{s} {ans}')
