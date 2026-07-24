# Dictionary & Set 메서드 정리

---

# Dictionary (딕셔너리)

> **키(key)로 값을 찾는 자료구조**
>
> - 키는 중복 불가
> - 값은 중복 가능

---

## 1. get()

키를 안전하게 조회한다.

- 키가 있으면 값 반환
- 키가 없으면 `None` 반환
- 기본값 지정 가능

```python
person = {'name': 'Alice', 'age': 25}

print(person.get('name'))               # Alice
print(person.get('country'))            # None
print(person.get('country', 'Unknown')) # Unknown
```

> `person['country']`는 KeyError 발생

---

## 2. keys(), values(), items()

### keys()

키만 반환

```python
person.keys()
```

```python
for key in person.keys():
    print(key)
```

---

### values()

값만 반환

```python
for value in person.values():
    print(value)
```

---

### items()

(키, 값) 튜플 반환

```python
for key, value in person.items():
    print(key, value)
```

---

## 3. setdefault()

조회하면서 없으면 추가

- 키가 있으면 기존 값 반환
- 키가 없으면 추가 후 반환

```python
person = {'name':'Alice'}

person.setdefault('country', 'KOREA')

print(person)
```

```
{'name':'Alice', 'country':'KOREA'}
```

> `get()`과 달리 딕셔너리가 변경된다.

---

## 4. update()

딕셔너리 갱신

- 같은 키 → 덮어쓰기
- 없는 키 → 추가

```python
person = {'name':'Alice', 'age':25}

person.update({'name':'Jane', 'country':'KOREA'})
```

```
{'name':'Jane', 'age':25, 'country':'KOREA'}
```

키워드 인자도 가능

```python
person.update(age=100, address='SEOUL')
```

---

## 5. pop()

키를 삭제하고 값 반환

```python
person.pop('age')
```

```
25
```

기본값 지정 가능

```python
person.pop('country', None)
```

---

## 6. clear()

모든 요소 삭제

```python
person.clear()
```

```
{}
```

---

# Set (세트)

> **중복 없는 자료구조**
>
> - 순서 없음
> - 인덱싱 불가

---

## 1. add()

원소 하나 추가

```python
my_set.add(4)
```

이미 있는 값이면 아무 변화 없음.

---

## 2. update()

여러 원소 한 번에 추가

```python
my_set.update([1,4,5])
```

리스트의 `extend()`와 비슷하다.

---

## 3. remove()

원소 삭제

```python
my_set.remove(2)
```

없는 값 삭제 시 `KeyError`

---

## 4. discard()

원소 삭제

```python
my_set.discard(2)
```

없는 값이어도 에러가 발생하지 않는다.

---

## 5. pop()

임의의 원소 하나를 꺼내며 삭제

```python
element = my_set.pop()
```

세트는 순서가 없으므로 어떤 값이 나올지는 보장되지 않는다.

---

## 6. clear()

모든 원소 삭제

```python
my_set.clear()
```

```
set()
```

> 빈 세트는 `{}`가 아니라 `set()`이다.

---

# 집합 연산

```python
set1 = {0,1,2,3,4}
set2 = {1,3,5,7,9}
```

| 메서드 | 연산자 | 의미 |
|---------|:------:|------|
| `difference()` | `-` | 차집합 |
| `intersection()` | `&` | 교집합 |
| `union()` | `\|` | 합집합 |
| `issubset()` | `<=` | 부분집합 |
| `issuperset()` | `>=` | 상위집합 |

```python
set1.difference(set2)
# {0,2,4}

set1.intersection(set2)
# {1,3}

set1.union(set2)
# {0,1,2,3,4,5,7,9}

set1.issubset(set2)
# False

set1.issuperset(set2)
# False
```

---

# 자주 헷갈리는 메서드

| 자료형 | 하나 추가 | 여러 개 추가 | 삭제 |
|---------|----------|-------------|------|
| list | `append()` | `extend()` | `pop()` |
| set | `add()` | `update()` | `remove()`, `discard()`, `pop()` |
| dict | `dict[key]=value` | `update()` | `pop()` |
