a = int(input())

for i in range(1,a+1):
    n,m = map(int,input().split())
    
    kill = 0  #테스트 케이스 마다 최댓값 초기화
    arr = [] #파리가 앉아 있을 초기 배열
    for _ in range(n):
        ans = list(map(int, input().split())) #우선 한줄 단위로 받기
        arr.append(ans) #반복문 만큼 리스트를 받아내고, 다시 그 줄을 전체 배열에 추가

    for a in range(n-m+1): #전체 배열 안에서 파리채 이동시키기
        for b in range(n-m+1):

            sum = 0 #한 파리채 당의 파리 개수 초기화
            for x in range(m): #파리채 크기안의 파리 숫자 구하기
                for y in range(m):
                    sum += arr[a+x][b+y] #합계에 1파리채 스윙 사살 개수 더하기
        
            if sum > kill: #이번 스윙에 사살 값이 최댓값보다 크다?
                kill = sum #최댓값 교체
    
    print(f'#{i} {kill}') #출력

        