t = int(input())

for c in range(1, t+1):
    num = int(input()) #숫자 입력받음
    sheep = set() # 세트 생성
    cnt = 1 #배수 숫자

    while (len(sheep) != 10): #세트의 길이가 10인경우 멈추기
        #즉 0~9의 숫자가 모두 모였다면 멈추기

        ans = num * cnt #배수 생성
        answer = str(ans) #나온 배수 값을 문자열로 만들고,

        for s in answer: #그 문자열을 하나씩 돌며 세트에 추가
            sheep.add(s) #세트는 append 가 아니라 add로 추가

        cnt += 1 #배수 확인 후 배수 카운트 증가
    print(f'#{c} {answer}')