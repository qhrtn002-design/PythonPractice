t = int(input())

for i in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    print(f'#{i} ',end='')
    print(*arr) #해당 리스트 대활호 빼고 모두 출력