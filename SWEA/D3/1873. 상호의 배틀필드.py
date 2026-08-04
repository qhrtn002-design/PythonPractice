dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
t = int(input())
for s in range(t):
    h, w = map(int,input().split())
    arr = [list(input()) for _ in range(h)]
    n = int(input())
    move = input()
    


    print(f'#{s+1}',end='')
    for row in arr:
        print(*row)
# 문자	의미
# .	평지(전차가 들어갈 수 있다.)
# *	벽돌로 만들어진 벽
# #	강철로 만들어진 벽
# -	물(전차는 들어갈 수 없다.)
# ^	위쪽을 바라보는 전차(아래는 평지이다.)
# v	아래쪽을 바라보는 전차(아래는 평지이다.)
# <	왼쪽을 바라보는 전차(아래는 평지이다.)
# >	오른쪽을 바라보는 전차(아래는 평지이다.)