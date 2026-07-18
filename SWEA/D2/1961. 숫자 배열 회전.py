def rotate(arr): #돌리는 함수 생성
    newarr= [] #새 배열 지정
    for _ in range(len(arr)): #주어진 배열의 길이만큼 반복해서
        newarr.append([0]*len(arr)) #기본칸이 0으로 채워진 새 배열 완성

    for j in range(len(arr)): #원본 배열의 열 번호를 순서대로 선택
        for i in range(len(arr)): #선택한 열의 모든 행을 확인
            newarr[j][len(arr)-1-i] = arr[i][j]
            # 원본의 (행 i, 열 j)에 있는 값을
            # 회전 후 (행 j, 열 n-1-i) 위치로 이동

            # j는 새로운 행이 되고,
            # 기존 행 번호 i는 반대로 뒤집혀 새로운 열 번호가 된다.

    return newarr #새 배열 리턴

t = int(input())
for c in range(1,t+1):
    n = int(input())
    arr = [] #이건 주어진 배열을 받기 위한 배열 생성

    for _ in range(n):
        ans = list(map(int, input().split()))
        arr.append(ans) #문제에서 주어진 배열 받기

    arr90 = rotate(arr) #90도 회전한 배열을 저장
    arr180 = rotate(arr90) #180도 회전한 배열을 저장
    arr270 = rotate(arr180) #270도 회전한 배열을 저장

    print(f'#{c}')
    for i in range(len(arr)):
        # 3개의 배열에서 같은 행 모두 선택
        print(''.join(map(str,arr90[i])),
              #그 행의 숫자를 여백없는 문자열로 변환 후 출력
               ''.join(map(str,arr180[i])),
               ''.join(map(str,arr270[i])))
   