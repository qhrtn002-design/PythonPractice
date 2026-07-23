a = [5,3,2,3,54,6,3,2,1,2,3]
ans = a[0]
for i in range(len(a)):
    if a[i] > ans:
        ans = a[i]
        max_val_idx = i
print(ans)
print(max_val_idx)


#3 a에서 최대 빈도수를 갖는 숫자를 출력하세요.
cnt = 0

for i in range(len(a)):
    count = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            count += 1

    if count > cnt:
        cnt = count
        answer = a[i]

print(answer)