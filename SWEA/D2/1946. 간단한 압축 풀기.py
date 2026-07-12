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


          
            
# cnt 카운팅 없이 풀이
n = int(input()) # 테스트 케이스 입력

for i in range(1,n+1):
    s = int(input()) # 케이스 내 반복 횟수 받기
    ans = '' #출력 받을 문자열 생성
    print(f'#{i}')
    for i in range(1,s+1):
        x,y = input().split() #문자 및 숫자 받기

        ans += x * int(y) #문자열에 문자 * 숫자만큼 받기
    for i in range(0,len(ans),10): #출력 반복문
        # i 는 10, 20, 30...10단위 증가
        # 문자열을 10글자씩 잘라 출력하기 위한 시작 위치 조정. 시작점만 잡기

        print(ans[i:i+10]) #문자열을 슬라이싱, 10개 단위로 출력
    print()