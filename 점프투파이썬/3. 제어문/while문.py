treehit = 0
while treehit < 10:
    treehit += 1
    print("나무를 %d 번 찍었습니다." % treehit)

    if treehit == 10:
        print("나무 넘어갑니다.")


prompt = """

1. add
2. del
3. list
4. quit

Enter number : """

number = 0
while number != 4:
    print(prompt, end = '') #줄 바꿈 없애기
    number = int(input())


a = 0
while a<10:
    a += 1
    if a%3 == 0:
        continue
    print(a)


