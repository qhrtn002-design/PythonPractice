t = int(input())
for s in range(1, t+1):
    n = input()
    cnt = 0
    ball = 0
    for i in n:
        if i == '(' or i == ')':
            cnt += 1 #공발견시 카운팅
    for j in range(len(n)):
        if n[j] == '(' and n[j+1] == ')':
            ball += 1 #전체 리스트에서 띄어진 공 개수 구하기

    ans = cnt - ball #둘을 빼서 최소의 공개수 구하기
    print(f'#{s} {ans}')