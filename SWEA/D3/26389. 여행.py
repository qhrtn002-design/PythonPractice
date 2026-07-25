t = int(input())
dir = {'N':'S', 'S':'N', 'W':'E', 'E':'W'}
for s in range(1,t+1):
    trip = input()
    ans = 'Yes'
    for i in trip: #이동한 방향 문자열 반복
        if dir.get(i) not in trip:
        #만약 이동한 방향을 키로 한 value가 문자열에 없다면, 돌아갈수 없고 거리도 못잰다.
            ans = 'No'
                
    print(ans)