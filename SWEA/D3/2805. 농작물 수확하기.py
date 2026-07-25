t = int(input())

for s in range(1,t+1):
    num = int(input())
    
    arr = [list(map(int,input())) for _ in range(num)]

    center = num // 2 #센터 잡기
    total = 0 #합계 지정

    for i in range(num): 
        dis = abs(center - i) #배열길이 만큼 돌면서 중앙기준으로 거리재기
        total += sum(arr[i][dis: num-dis])
        # 칸 기준으로 행은 하나씩 반복하되 열은 슬라이싱으로 센터만큼 범위만 나오기
    print(f'#{s} {total}')