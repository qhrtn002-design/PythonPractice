n, m = map(int, input().split())
ans = [] # 스택 세팅
visited = [0] * (n + 1) #방문 배열 세팅
def perm(num): #함수 생성
    if num == m: #문제에서 시킨대로 m개 만큼 골랏냐?
        print(*ans) #골랐으면 출력하고 리턴
        return
    for i in range(1, n + 1): #안 골랐으면 1부터 반복
        if not visited[i]: # 아직 안 뽑은걸 방문배열로 확인 후
            visited[i] = 1 # 방문 배열 표시하고
            ans.append(i) #스택에 추가
            perm(num + 1) #재귀로 함수 호출 후 하나 넣었으니 num+1로 표시
            ans.pop() # 스택 최상단 빼고,
            visited[i] = 0 # 방문행렬은 다시 0으로 수정
perm(0)

def comb(num, idx):
    if num == m:
        print(*ans)
        return
    for i in range(idx, n):
        ans.append(i)
        comb(num+1, i)
        ans.pop()

comb(0,0)

def dup_perm(num):
    if num == m:
        print(*ans)
        return
    for i in range(1,n+1):
        ans.append(i)
        dup_perm(num+1)
        ans.pop()

dup_perm(0)

def dup_comb(num, idx):
    if num == m:
        print(*ans)
        return
    for i in range(idx, n):
        ans.append(i)
        dup_comb(num+1, i+1)
        ans.pop()

dup_comb(0,0)