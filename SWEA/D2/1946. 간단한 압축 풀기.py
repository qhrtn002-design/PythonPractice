a = int(input())

for z in range(1,a+1): #테스트 케이스 1부터 출력하기
    k = int(input()) #테스트 개수 받기
    cnt = 0 # 글자수 카운트
    print(f'#{z}')

    for i in range(k):
        x, y = input().split()

        for j in range(int(y)): #글자를 뒤에 숫자 만큼 카운팅
            print(x,end='')
            cnt += 1 # 글자수 하나당 카운팅

            if cnt % 10 == 0:
                print() # 글자수 10단위로 줄바꿈
    print() #전체 끝나서 다시 줄바꿈
            