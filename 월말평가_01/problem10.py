############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 별도 라이브러리 없이 구현합니다.
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def simulate_drone(grid, start, commands):
    dir = 0
    position = list(start)
    for i in commands:
        if i == 'F':
            nx = position[0] + dx[dir]
            ny = position[1] + dy[dir]
            if 0<=nx<len(grid) and 0<=ny<len(grid) and grid[nx][ny] != 1:
                position[0] = nx
                position[1] = ny
        elif i =='R':
            dir = (dir+1) % 4
        elif i == 'L':
            dir = (dir-1) % 4
    return tuple(position)
            
    # 여기에 코드를 작성하여 함수를 완성합니다.

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
# grid: 0 = 비행 가능, 1 = 장애물
# 시작 방향은 위쪽(상), 좌표는 (row, col), R=시계/L=반시계 회전
# 전진하려는 칸이 격자 밖이거나 장애물이면 그 전진 명령은 무시
grid = [[0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]]
# 1) (0,0) 상 -> F: 위는 격자 밖 -> 무시
# 2) R -> 우를 봄
# 3) F: (0,1) 이동 / 4) F: (0,2) 이동
# print(simulate_drone(grid, (0, 0), "FRFF"))  # (0, 2)
# 1) (2,1) 상 -> F: (1,1) 장애물 -> 무시
# 2) R -> 우 / 3) F: (2,2) 이동 / 4) F: (2,3) 격자 밖 -> 무시
# print(simulate_drone(grid, (2, 1), "FRFF"))  # (2, 2)
#####################################################
print(simulate_drone(grid, (0, 0), "FFRFF"))
# (0, 2)

print(simulate_drone(grid, (2, 0), "FRFRF"))
# (2, 0)

print(simulate_drone(grid, (1, 2), "LFF"))
# (1, 2)

print(simulate_drone(grid, (2, 1), "LFRF"))
# (2, 0)

print(simulate_drone(grid, (0, 1), "RFLFFR"))
# (0, 1)