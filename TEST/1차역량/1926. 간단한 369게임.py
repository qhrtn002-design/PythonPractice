n=int(input())
for i in range(1,n+1):
    cnt=0
    for k in str(i):
        if k in '369':
            cnt+=1
    if cnt>0:
        print('-'*cnt,end=' ')
    else:
        print(i,end=' ')