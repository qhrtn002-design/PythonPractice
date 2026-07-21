t = int(input())

def count(v):
    if v == 0: #자식이 없으면 개수 0
        return 0
    return 1+count(left[v])+count(right[v]) #자기자신 + 왼쪽노드 + 오른쪽 노드를 재귀로 반복

for s in range(1,t+1):
    e, n = map(int, input().split())

    lst = list(map(int,input().split()))
    left = [0] * (e+2) #노드 번호를 인덱스로 사용하기 위해 왼쪽 자식배열 생성
    right = [0] * (e+2) #오른쪽 자식 배열 생성

    for i in range(0, len(lst), 2): #트리 만들기 반복문
        p = lst[i] #부모 노드 번호
        q = lst[i+1] #자식 노드 번호

        if left[p] == 0: #왼쪽 자식이 비었으면 
            left[p] = q #왼쪽에 채우고
        else: #왼쪽이 이미 있으면
            right[p] = q #오른쪽에 채우기

    print(f'#{s} {count(n)}')

