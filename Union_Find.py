# Union-Find
# 각각의 독립된 데이터를 그룹화 시킨 후 관리.
# 그래프의 사이클 존재여부도 확인가능

# union(0,1) 이라는 함수를 제작.
# 0이 속한 그룹과 1이 속한 그룹이 하나로 합쳐짐

arr = [i for i in range(6)]
rank = [0]*6

def union(a,b):
    fa = findboss(a)
    fb = findboss(b)
    if fa == fb: # 두 보스가 같으면 이미 같은 그룹
        return

    # arr[fb] = fa # 보스가 다르면 a의 보스가 통이 됨

    if rank[a] == rank[b]:
        rank[a]+=1
        arr[fb] = fa
    elif rank[a] > rank[b]:
        arr[fb] = fa
    else:
        arr[fa] = fb

def findboss(member):
    if arr[member] == member: # 자기자신이 보스면 (보스찾음)
        return member
    ret = findboss(arr[member]) # 보스가 아니라면 arr배열의 값을 가지고 보스 찾기
    arr[member] = ret # 경로 단축
    return ret

union(0,1)
union(3,4)
union(1,4)
union(1,3)
union(5,4)

x,y = map(int,input().split())

if findboss(x) == findboss(y):
    print('같은 그룹')
else:
    print('다른 그룹')