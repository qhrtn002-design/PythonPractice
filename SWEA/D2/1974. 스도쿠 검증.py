t = int(input())

for s in range(1,t+1):
    flag = 1
    ans = []

    for x in range(9): #행(가로) 스도쿠 검사
        arr = list(map(int, input().split()))
        ans.append(arr)
        if len(set(arr)) != 9:
            flag = 0
    
    for x in range(9): #열(세로) 스도쿠 검사
        col = []
        for y in range(9):
            col.append(ans[y][x])
        if len(set(col)) != 9:
            flag = 0
    
    for x in range(0,9,3): #3*3 격자 스도쿠 검사
        for y in range(0,9,3):
            test = []
            for i in range(3):
                for j in range(3):
                    test.append(ans[x+i][y+j])
            if len(set(test)) != 9:
                flag = 0
            
    print(f'#{s} {flag}')