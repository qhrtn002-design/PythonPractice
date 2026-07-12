a = int(input())

for tc in range(1, a+1):
    b = int(input()) #한계 줄 수는 케이스 안에서 받기
    print(f'#{tc}')
    prev = [] # 이전 줄 저장하기

    for i in range(b):
        lst = [] #지금 한 줄 받는 리스트
        for j in range(i+1):
            if j == 0 or j == i: #양 끝 인덱스가 0이거나 맨끝일때
                lst.append(1) #그냥 1로 출력
            else:
                lst.append(prev[j] + prev[j-1])
                #가운데라면 이전 줄의 값들을 더한 값으로 넣기
        prev = lst # 지금까지 구했던 lst 해당 줄을 이전 줄로 넘겨 저장하기
        
        print(*lst,end=' ') #리스트를 for문 없이 해당 줄만 출력하기
        print()