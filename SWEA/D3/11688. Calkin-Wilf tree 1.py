t = int(input())

for s in range(1,t+1):
    n = input()

    start = 1,1
    for i in n:
        if i == 'L': #L이면 조건에 맞게 자식노드 생성
            node = start[0], start[0]+start[1]
        else:
            node = start[0]+start[1], start[1]
        start = node #자식노드가 다시 시작노드가 됨

    print(f'#{s} ', end = '')
    print(*node)