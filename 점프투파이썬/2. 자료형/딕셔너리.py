a = {1: 'a'}
a[2] ='b' #{2:'b} 쌍을 추가
print(a)

a['name'] = 'SEO'
print(a)

a[3] = [1,2,3]
print(a)

del a[1] #del은 print 내부에 들어갈 수 없다.
print(a)

grade = {'pey': 10, 'julliet': 99}
print(grade['pey']) # key가 pey인 value 반환


s={'name':'Seo', 'phone':'010-5270-9628','birth':'0926'}
print(s.keys()) #keys 뒤에 괄호 필수
print(list(a.keys())) #key들을 다시 리스트로 반환

print(s.values()) #values 뒤에 괄호 필수
print(list(s.values())) #value들을 다시 리스트로 반환
print(s.items()) #items 뒤에 괄호 필수)
print(list(s.items())) #item들을 다시 리스트로 반환

print(s.get('name')) #괄호 형태 없이 원소만 출력