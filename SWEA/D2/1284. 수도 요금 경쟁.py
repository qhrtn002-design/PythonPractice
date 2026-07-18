t = int(input())

for c in range(1,t+1):
    p, q, r, s, w = map(int, input().split()) 

    A = p*w # A회사 요금 계산
    if w < r: #사용량이 R 이하인 경우
        B = q #B회사는 그냥 기본요금
    else: #사용량이 R 이상이면
        B = (w-r) * s + q #기본 요금 + 초과리터 당 S원

    if A > B: # A, B 둘 중 저렴한 회사로 선택
        ans = B
    else:
        ans = A
    print(f'#{c} {ans}')