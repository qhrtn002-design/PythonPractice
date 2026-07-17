num = int(input())

for i in range(1,num+1):
    lst = list(map(int, input().split())) #리스트로 받기
    lst.sort() #리스트 정렬
    
    total = sum(lst[1:9]) #슬라이싱으로 최대,최소값 자르기

    print(f'#{i} {round(total/8)}') #평균 출력 후 반올림