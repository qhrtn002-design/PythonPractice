a = int(input())

arr = list(map(int, input().split())) #공백으로 나눈 리스트 받기
arr.sort() #오름차순 정렬
print(arr[a//2]) # 중간값 출력, 길이 절반 나누기