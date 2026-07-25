t = int(input())
dir = {'N':'S', 'S':'N', 'W':'E', 'E':'W'}
for s in range(1,t+1):
    trip = input()
    ans = 'Yes'
    for i in trip:
        if dir.get(i) not in trip:
            ans = 'No'
                
    print(ans)