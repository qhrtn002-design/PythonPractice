# Python 리스트 메서드

---

# 1. 리스트(List) 메서드

## 리스트란?

리스트(List)는 **여러 개의 값을 순서대로 저장하는 자료형**이다.

리스트는 **가변(Mutable) 객체**이므로, 대부분의 메서드는 **원본 리스트를 직접 수정**한다.

```python
numbers = [1, 2, 3]
```

---

## 리스트 메서드의 특징

문자열과 가장 큰 차이점은 **원본이 변경된다**는 것이다.

대부분의 리스트 메서드는

- 원본 리스트를 수정한다.
- 반환값이 `None`이다.
- 따라서 결과를 변수에 저장할 필요가 없다.

예시

```python
numbers = [1, 2, 3]

numbers.append(4)

print(numbers)
```

결과

```python
[1, 2, 3, 4]
```

반면

```python
new = numbers.append(5)

print(new)
```

결과

```python
None
```

---

## 문자열과 리스트 비교

|구분|문자열(str)|리스트(list)|
|---|---|---|
|객체 종류|불변(Immutable)|가변(Mutable)|
|메서드 호출 후|새 문자열 반환|원본 수정|
|반환값|새 문자열|대부분 None|

---

# 2. 요소 추가

---

# append()

## 기능

리스트의 **맨 뒤에 요소 하나**를 추가한다.

---

### 문법

```python
리스트.append(값)
```

---

### 예제

```python
numbers = [1, 2, 3]

numbers.append(4)

print(numbers)
```

결과

```python
[1, 2, 3, 4]
```

---

### 주의

```python
numbers = [1, 2, 3]

result = numbers.append(4)

print(result)
```

결과

```python
None
```

---

### 한 줄 요약

> 리스트의 맨 뒤에 요소 **하나**를 추가한다.

---

# extend()

## 기능

리스트나 문자열처럼 **순회 가능한(iterable) 객체의 요소를 하나씩 추가**한다.

---

### 문법

```python
리스트.extend(반복가능한객체)
```

---

### 예제

```python
numbers = [1, 2, 3]

numbers.extend([4, 5, 6])

print(numbers)
```

결과

```python
[1, 2, 3, 4, 5, 6]
```

---

### 문자열도 가능

```python
letters = ['A']

letters.extend("BCD")

print(letters)
```

결과

```python
['A', 'B', 'C', 'D']
```

---

### 주의

```python
numbers.extend(100)
```

결과

```python
TypeError
```

숫자는 반복 가능한 객체가 아니기 때문이다.

---

# append() vs extend()

이 둘은 가장 많이 헷갈리는 메서드이다.

```python
numbers = [1, 2, 3]

numbers.append([4, 5])

print(numbers)
```

결과

```python
[1, 2, 3, [4, 5]]
```

리스트 하나가 통째로 들어간다.

---

```python
numbers = [1, 2, 3]

numbers.extend([4, 5])

print(numbers)
```

결과

```python
[1, 2, 3, 4, 5]
```

리스트를 풀어서 각각 추가한다.

---

## 비교

|메서드|추가 방식|
|---|---|
|append()|객체 하나 추가|
|extend()|요소를 하나씩 추가|

---

# insert()

## 기능

원하는 위치에 값을 삽입한다.

뒤에 있는 요소들은 한 칸씩 밀려난다.

---

### 문법

```python
리스트.insert(인덱스, 값)
```

---

### 예제

```python
numbers = [1, 2, 3]

numbers.insert(1, 100)

print(numbers)
```

결과

```python
[1, 100, 2, 3]
```

---

### 한 줄 요약

> 원하는 위치에 요소를 삽입한다.

---

# 3. 요소 삭제

---

# remove()

## 기능

값을 찾아 **처음 만나는 요소 하나만 삭제**한다.

---

### 문법

```python
리스트.remove(값)
```

---

### 예제

```python
numbers = [1, 2, 2, 3]

numbers.remove(2)

print(numbers)
```

결과

```python
[1, 2, 3]
```

---

### 주의

```python
numbers.remove(100)
```

결과

```python
ValueError
```

없는 값을 삭제하면 에러가 발생한다.

---

# pop()

## 기능

인덱스를 이용하여 요소를 삭제하고

삭제한 값을 반환한다.

---

### 문법

```python
리스트.pop()

리스트.pop(인덱스)
```

---

### 예제

```python
numbers = [1, 2, 3, 4]

item = numbers.pop()

print(item)
print(numbers)
```

결과

```python
4

[1, 2, 3]
```

---

맨 앞 삭제

```python
numbers = [1, 2, 3]

item = numbers.pop(0)

print(item)
print(numbers)
```

결과

```python
1

[2, 3]
```

---

## remove()와 pop() 비교

|메서드|삭제 기준|반환값|
|---|---|---|
|remove()|값|없음(None)|
|pop()|인덱스|삭제한 값|

---

# clear()

## 기능

리스트의 모든 요소를 삭제한다.

---

### 예제

```python
numbers = [1, 2, 3]

numbers.clear()

print(numbers)
```

결과

```python
[]
```

---

# 4. 순서 변경

---

# reverse()

## 기능

현재 순서를 그대로 뒤집는다.

**정렬이 아니다.**

---

### 예제

```python
numbers = [1, 3, 2, 8]

numbers.reverse()

print(numbers)
```

결과

```python
[8, 2, 3, 1]
```

---

### 특징

- 원본 변경
- 반환값 None

---

# sort()

## 기능

리스트를 정렬한다.

기본은 오름차순이다.

---

### 문법

```python
리스트.sort()
```

---

### 예제

```python
numbers = [3, 1, 100, 2]

numbers.sort()

print(numbers)
```

결과

```python
[1, 2, 3, 100]
```

---

## 내림차순

```python
numbers.sort(reverse=True)

print(numbers)
```

결과

```python
[100, 3, 2, 1]
```

---

### 특징

- 원본 변경
- 반환값 None

---

# sort() vs sorted()

이 둘은 반드시 구분해야 한다.

---

## sort()

```python
numbers = [3, 2, 1]

numbers.sort()

print(numbers)
```

결과

```python
[1, 2, 3]
```

- 리스트 메서드
- 원본 변경
- 반환값 None

---

## sorted()

```python
numbers = [3, 2, 1]

new_numbers = sorted(numbers)

print(numbers)
print(new_numbers)
```

결과

```python
[3, 2, 1]

[1, 2, 3]
```

- 내장 함수
- 원본 유지
- 새로운 리스트 반환

---

## 비교

|구분|sort()|sorted()|
|---|---|---|
|종류|리스트 메서드|내장 함수|
|원본 변경|O|X|
|반환값|None|새 리스트|

---

# 리스트 메서드 정리

|메서드|기능|
|---|---|
|append()|맨 뒤에 요소 하나 추가|
|extend()|요소 여러 개 추가|
|insert()|원하는 위치에 삽입|
|remove()|값으로 삭제|
|pop()|인덱스로 삭제 후 반환|
|clear()|전체 삭제|
|reverse()|순서 뒤집기|
|sort()|정렬|

---

# 반드시 기억할 것 ⭐

✅ 리스트는 **가변(Mutable)** 객체이다.

✅ 대부분의 리스트 메서드는 **원본을 직접 수정**한다.

✅ 대부분의 리스트 메서드는 **None을 반환**한다.

✅ `append()`는 하나를 추가하고, `extend()`는 여러 요소를 추가한다.

✅ `remove()`는 값으로 삭제, `pop()`은 인덱스로 삭제하면서 값을 반환한다.

✅ `reverse()`는 **순서만 뒤집을 뿐 정렬이 아니다.**

✅ 원본을 유지하며 정렬하려면 **`sorted()`** 를 사용한다.