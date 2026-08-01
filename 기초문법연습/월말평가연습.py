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