n = int(input()) #테스트 케이스 받기

for i in range(1,n+1): #369 시작
    cnt = 0
    for j in str(i): # 369 숫자중 3,6,9 검색하는 j
        if j in '369':
            cnt += 1 # j가 3,6,9에 해당하면 카운팅
    if cnt > 0:
        print("-"*cnt,end=' ') #카운트하면서 박수(-) 출력
    else: 
        print(i, end=' ') #아니면 그냥 숫자 출력



        