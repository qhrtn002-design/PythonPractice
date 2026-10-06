def union(a,b):
    fa = find(a) # A에서 가리키는 최종 목적지
    fb = find(b) # B에서 가리키는 최종 목적지
    if fa!=fb: # 만약 그 목적지가 다르다면
        group[fa] = fb # 그 둘 도 하나로 향하게끔 유니온
    
def find(x): # 최종목적지 찾는 함수
    if group[x] != x: # 만약 현재 수가 최종목적지가 아니라면
        x = find(group[x]) # 계속 찾아라
    return group[x] # 최종 목적지 리턴

t=int(input())
for tc in range(t):
    n,m=map(int,input().split())
    group=[i for i in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        union(a,b) # 유니온 시작

    ans = set()
    for i in range(1,n+1): # 1부터 n까지 반복해서
        ans.add(find(i)) # 반복 속에 나눠진 그룹들을 집합에 더함

    print(f'#{tc+1} {len(ans)}')