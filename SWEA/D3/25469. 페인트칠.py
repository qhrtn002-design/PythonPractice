t = int(input())

for s in range(1,t+1):
    h, w = map(int, input().split())
    arr = [(list(input()))for _ in range(h)] #배열 생성
    
    row = 0 #색칠한 행 개수 초기값
    for i in range(h):
        cnt = 0 #행마다 카운팅하니까 여기서 초기화
        for j in range(w):
            if arr[i][j] == '#': #색칠되었으면 카운팅
                cnt += 1
        if cnt == w: #총 카운팅이 길이와 같으면 그 줄은 색칠된것
            row +=1 #색칠 행 개수 추가

    col = 0 #색칠한 열 개수 초기값
    for i in range(w):
        cnt = 0 #열마다 카운팅
        for j in range(h):
            if arr[j][i] == '#': #열부터 따지므로 인덱스 전환
                cnt += 1
        if cnt == h:
            col +=1

    ans = 0
    if row == h and col == w: #만약 3*5배열에서 모두 칠해진 경우
        ans = min(row, col) #가장 작은 길이로 쭉 페인트한것 (세로로)
    else:
        ans = row + col #아니면 그냥 두개 더해서 칠한 줄 개수 구하기

    print(ans)