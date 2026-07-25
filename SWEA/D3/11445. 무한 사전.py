t = int(input())
for s in range(1,t+1):
    p = input().strip() #쓰레기값 공백제거
    q = input().strip()
    ans = 'Y' #기본값 Y세팅
    if q == p + 'a': #하나라도 이 조건이면 n출력
        # 문자열 길이가 같은데 p에 a만 추가되야 q여야 사이에 문자가 없다.
        ans = 'N'
    print(f'#{s} {ans}')