T = int(input())

for tc in range(1, T + 1):
    text = input() #문자열 받기

    for t in range(1, 11): #최대 마디만큼 단어길이 늘려보기
        pat = text[:t] #처음 지정하는 패턴
        flag = 1 #현재 가정한 마디가 맞는지 표시

        for j in range(t, len(text)): #마디 부터 전체 문자열까지 반복
            if text[j] != text[j - t]: #현재 문자와 t칸 앞의 문자가 다르면?
                flag = 0 #해당 t는 마디길이가 아님
                break

        if flag: 
            answer = t # 지금 t가 마디 길이가 맞다
            break

    print(f'#{tc} {answer}')