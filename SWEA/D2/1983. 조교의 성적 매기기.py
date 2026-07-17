t = int(input())

for i in range(1, t+1):
    n, k = map(int, input().split()) #학생 수, 몇 번째 학생?

    score = [] #총점과 학생 번호를 저장할 리스트 생성
    for x in range(n):
        mid, fin, task = map(int, input().split()) #중간 기말 과제
        total = mid * 0.35 + fin * 0.45 + task * 0.2 #각 비율에 맞게 총합계산
        score.append((total,x+1)) #총합 계산 후, 학생 번호달고 튜플 형식으로 리스트 삽입

    score.sort(reverse=1) #내림차순 정렬

    grade = ["A+","A0","A-","B+","B0","B-","C+","C0","C-","D0"] #성적 리스트 입력
    cnt = n // 10 #한 등급당 학생 수 계산

    for idx, value in enumerate(score): #인덱스, 값 형식으로 반복문 실행
        if value[1] == k: #만약 value의 두번째 값인 학생번호가 찾고 있는 K이면
            ans = grade[idx//cnt] # 학생의 순위를 등급구간으로 적용하여 학점 결정

    print(f'#{i} {ans}')