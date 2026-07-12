a = int(input()) 

for _ in range(1,a+1):
    s = int(input()) #초 수 받기
    sp = 0 #속도 저장
    m = 0 # 거리 저장

    for i in range(s): # 초 만큼 반복
        cmd = list(map(int, input().split())) # 가속여부, 속도 받기
        # 0일땐 속도가 나오지 않으므로 리스트로 받음. 두개가 아닌 하나여도 오류 안남

        if cmd[0] == 1: #가속인 경우
            sp += cmd[1] #기존 속도에 가속만큼 추가
            
        elif cmd[0] == 2: #감속인 경우
            sp -= cmd[1] #기존 속도에 감속만큼 빼기
            if sp<=0: 
                sp = 0 #속도는 마이너스가 나올 수 없으므로 0으로 하한선 지정
            
        m += sp #다하고 나서 총 거리만큼 속도 더하기

    print(f'#{_} {m}')