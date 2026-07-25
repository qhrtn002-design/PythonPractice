t = int(input())
color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
# 색 리스트 설정
for s in range(1,t+1):
    a, b = input().split()
    if a in color:
        n1 = color.index(a) # 첫번째 색의 인덱스 저장
    if b in color:
        n2 = color.index(b) # 두번째 색의 인덱스 저장

    dis = abs(n1-n2) #인덱스간의 거리 저장
    if dis == 0: #거리에 따른 결과값 출력
        ans = 'E'
    elif dis == 1:
        ans = 'A'
    elif dis == 2:
        ans = 'X'
    elif dis == 3:
        ans = 'C'
    elif dis == 4:
        ans = 'X'
    elif dis == 5:
        ans = 'A'

    print(ans)