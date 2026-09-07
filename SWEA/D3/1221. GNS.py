t=int(input())
num = {"ZRO": 0,"ONE": 1,"TWO": 2,"THR": 3,"FOR": 4,"FIV": 5,"SIX": 6,"SVN": 7,"EGT": 8,"NIN": 9}
text= ['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']
for s in range(t):
    tc,n=input().split()
    lst=input().split()
    ans=[0]*10
    for i in lst:
        ans[num[i]]+=1
    print(tc)
    result=[]
    for i in range(10):
        for _ in range(ans[i]):
            result.append(text[i])
    print(*result)