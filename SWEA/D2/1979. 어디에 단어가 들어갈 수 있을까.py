t = int(input())

for c in range(1,t+1):
    n, k = map(int, input().split()) #배열 크기 및 단어길이 받기
    arr = [] #배열 생성
    for _ in range(n):
        num = list(map(int, input().split()))
        arr.append(num) #받은 배열 저장
    
    col = 0 #정답 생성 테스트케이스 마다 초기화 되므로 여기에 위치
    for i in range(n): #가로 계산
        cnt = 0 # 1의 연속 길이 카운트
        for j in range(n):
            if arr[i][j] == 1:
                cnt +=1 #배열에서 1이 발견될때 마다 1의 길이추가
            else:
                if cnt == k: # 1의 연속이 끝났으므로 길이 확인
                    col +=1 #맞다면 정답 +1
                cnt = 0 #1길이는 다시 초기화
        if cnt == k: #행이 1로 끝났을 때도, 그때 연속 길이가 단어와 같다면
            col +=1 #정답 +1

    for j in range(n): #세로 계산
        cnt = 0
        for i in range(n):
            if arr[i][j] == 1: #가로 계산 할때와 동일
                cnt += 1
            else:
                if cnt == k:
                    col +=1
                cnt = 0
        if cnt == k:
            col +=1

    print(f'#{c} {col}')