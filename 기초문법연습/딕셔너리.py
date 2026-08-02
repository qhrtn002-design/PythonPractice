temp = {'메로나':1000,'폴라포':1200,'빵빠레':1800}
temp['죠스바'] = 1200 #이렇게 항목을 추가하는것이 가장 보편적인가?
temp['월드콘'] = 1500 #만약 여러 항목의 키와 밸류를 한번에 추가하려며 어떻게 해야되는가?
#add는 딕셔너리에서 안쓰는건가?
temp['메로나'] = 1300  #update?는 언제 쓰는건가? 아예 쓸일이 없나?
print(f'메로나 가격: {temp["메로나"]}')
# 이렇게 value의 값을 불러오는게 딕셔너리이름 + 리스트 형태 안에 키값 넣는거랑, 
# 딕셔너리이름에 .get 으로 부르는거랑. 또 있나?
del temp['메로나']
temp.update(엔초=1800,가르나초=200)
print(temp)

def count_char_get(chars):
    ans = {}
    for i in chars:
        ans[i] = ans.get(i,0)+1
    return ans

from collections import defaultdict
def count_char_default(chars):
    cnt = defaultdict(int)
    for i in chars:
        cnt[i] += 1
    return dict(cnt)

def group_subjects(subjects):
    lst = defaultdict(list)
    for i,j in subjects:
        lst[i].append(j)
    return dict(lst)