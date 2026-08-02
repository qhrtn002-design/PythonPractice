def min_score(lst):
    n = lst[0]
    for i in range(len(lst)):
        if lst[i] < n:
            n = lst[i]
    return n


def under_60(lst):
    cnt = 0
    for i in lst:
        if i <60:
            cnt +=1
    return cnt


def is_user_data_valid(user_data):
    if user_data['id'] == "" or user_data['password'] == "":
        ans = False
    else:
        ans = True
    return ans


def is_id_valid(user_data):
    if '0' <= user_data['id'][-1] <= '9':
        return True
    return False

def max_score(lst):
    n = lst[0]
    for i in range(len(lst)):
        if lst[i]>=n:
            n = lst[i]
    return n

def average(lst):
    ans = 0
    for i in lst:
        ans += i
    return ans//(len(lst))

def passing(lst):
    cnt = 0
    for i in lst:
        if i >= 60:
            cnt += 1
    return cnt

def cnt_min(lst):
    n = lst[0]
    cnt = 0
    for i in range(len(lst)):
        if lst[i] < n:
            n = lst[i]
    for j in lst:
        if n == j:
            cnt += 1
    return cnt

def count_number(s):
    cnt = 0
    for i in s:
        if i in '0123456789':
            cnt += 1
    return cnt

def is_user_data_valid(user_data):
    if user_data['id'] == '' or user_data['password'] == '':
        return False
    return True

def is_adult(user_data):
    if user_data['age'] >=20:
        return True
    return False

def student_avg(students):
    ans = 0
    for i in students:
        ans += i['score']
    return ans/len(students)

def top_student(students):
    f_score = students[0]['score']
    f_name = students[0]['name']
    for i in students:
        if i['score'] >= f_score:
            f_score = i['score']
            f_name = i['name']
    return f_name


def total_price(products):
    ans = 0
    for i in products:
        ans += i['price']
    return ans

def count_food(products):
    cnt = 0
    for i in products:
        if i['category'] == 'food':
            cnt += 1
    return cnt

def is_password_valid(user_data):
    if len(user_data['password']) < 8:
        return False
    for i in user_data['password']:
        if i in '1234567890':
            return True
    return False


def get_grade(user_data):
    if user_data['purchase'] >= 100000:
        ans = 'VIP'
    elif user_data['purchase'] >= 50000:
        ans = 'GOLD'
    else:
        ans = 'SILVER'
    return ans 

def get_pass_students(students):
    ans = []
    for i in students:
        if i['score'] >= 60:
            ans.append(i['name'])
    return ans

def second_max(lst):
    arr = lst[:]
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if arr[i] > arr[j]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr[1]

def remove_duplicate(lst):
    ans = []
    for i in lst:
        if i not in ans:
            ans.append(i)
    return ans

def max_index(lst):
    n = lst[0]
    for i in range(len(lst)):
        if lst[i]>n:
            n = lst[i]
    for j in range(len(lst)):
        if lst[j] == n:
            ans = j
    return ans

def gil(text):
    cnt = 0
    for _ in text:
        cnt += 1
    return cnt