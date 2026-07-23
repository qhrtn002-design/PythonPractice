# Python 메서드(Method)와 문자열 메서드

---

# 1. 메서드(Method)란?

## 메서드란?

메서드(Method)는 **특정 자료형(객체)에 소속된 함수**이다.

쉽게 말하면 **그 자료형이 스스로 할 수 있는 기능**이라고 생각하면 된다.

메서드는 항상 **점(`.`)** 을 이용하여 호출한다.

```python
객체.메서드()
```

예시

```python
text = "Hello"
text.upper()

numbers = [1, 2, 3]
numbers.append(4)
```

---

## 함수와 메서드의 차이

### 함수(Function)

객체와 상관없이 이름만으로 호출한다.

```python
print("Hello")
len([1,2,3])
sorted([3,1,2])
```

호출 형태

```python
함수명(데이터)
```

---

### 메서드(Method)

특정 객체에 소속되어 있으며 점(`.`)을 이용해 호출한다.

```python
text.upper()
numbers.append(4)
```

호출 형태

```python
객체.메서드()
```

---

## 함수와 메서드 비교

|구분|함수|메서드|
|---|---|---|
|호출|`함수(데이터)`|`객체.메서드()`|
|소속|없음|특정 자료형|
|예시|`len()` `sorted()`|`append()` `upper()`|

---

## 자료형마다 메서드가 다르다

자료형마다 사용할 수 있는 메서드가 다르다.

예를 들어

```python
type("Hello")
```

결과

```python
<class 'str'>
```

```python
type([1,2,3])
```

결과

```python
<class 'list'>
```

문자열은 문자열 메서드를,

리스트는 리스트 메서드를 가진다.

---

## help()

어떤 자료형이 가진 메서드를 확인할 수 있다.

```python
help(str)

help(list)
```

---

# 2. 공통 시퀀스 메서드

시퀀스(sequence)

- 문자열(str)
- 리스트(list)
- 튜플(tuple)

처럼 **순서가 있는 자료형**을 말한다.

이 자료형들은 공통으로 사용할 수 있는 메서드가 있다.

---

# index()

## 기능

원하는 값이 **몇 번째 위치**에 있는지 반환한다.

가장 먼저 만나는 위치 하나만 반환한다.

없으면 **ValueError**가 발생한다.

---

### 문법

```python
시퀀스.index(값)
```

---

### 예제

```python
text = "banana"

print(text.index("a"))
```

결과

```python
1
```

```python
numbers=[1,2,3]

print(numbers.index(2))
```

결과

```python
1
```

---

### 주의

```python
text="banana"

text.index("z")
```

결과

```
ValueError
```

---

### 한 줄 요약

> 값을 찾으면 위치를 반환하고, 없으면 에러 발생

---

# count()

## 기능

특정 값이 몇 번 등장하는지 반환한다.

---

### 문법

```python
시퀀스.count(값)
```

---

### 예제

```python
text="banana"

print(text.count("a"))
```

결과

```python
3
```

```python
numbers=[1,2,2,3,3,3]

print(numbers.count(3))
```

결과

```python
3
```

---

### 특징

없는 값을 세더라도 에러가 발생하지 않는다.

```python
text.count("z")
```

결과

```python
0
```

---

### 한 줄 요약

> 값의 개수를 세며, 없으면 0을 반환한다.

---

# 3. 문자열 탐색 및 검증

---

# find()

## 기능

문자의 위치를 찾는다.

없으면 **-1**을 반환한다.

---

### 문법

```python
문자열.find(문자)
```

---

### 예제

```python
text="banana"

print(text.find("a"))
```

결과

```python
1
```

```python
print(text.find("z"))
```

결과

```python
-1
```

---

## index()와 find() 비교

|메서드|찾으면|없으면|
|------|------|------|
|index()|위치|ValueError|
|find()|위치|-1|

**코테에서는 없는 값도 처리해야 한다면 `find()`가 더 안전하다.**

---

# isupper()

## 기능

모든 알파벳이 대문자인지 검사한다.

```python
"HELLO".isupper()
```

결과

```python
True
```

```python
"Hello".isupper()
```

결과

```python
False
```

---

# islower()

## 기능

모든 알파벳이 소문자인지 검사한다.

```python
"hello".islower()
```

결과

```python
True
```

```python
"Hello".islower()
```

결과

```python
False
```

---

# isalpha()

## 기능

문자열이 **문자로만** 이루어져 있는지 검사한다.

숫자

공백

특수문자가 하나라도 있으면 False이다.

---

예제

```python
"Hello".isalpha()
```

결과

```python
True
```

```python
"123Hello".isalpha()
```

결과

```python
False
```

---

# 문자열 검증 메서드 요약

|메서드|설명|
|------|-----|
|isupper()|전부 대문자인가|
|islower()|전부 소문자인가|
|isalpha()|문자로만 이루어졌는가|

---

# 4. 문자열 조작 메서드

## 문자열은 불변(Immutable)

가장 중요한 특징이다.

문자열 메서드는 **원본을 절대 수정하지 않는다.**

항상 **새로운 문자열을 만들어 반환**한다.

```python
text="Hello"

text.upper()

print(text)
```

결과

```python
Hello
```

원본은 그대로이다.

반드시 저장해야 한다.

```python
text=text.upper()
```

---

# replace()

## 기능

문자열 일부를 다른 문자열로 바꾼다.

---

### 문법

```python
문자열.replace(기존,새로운)
```

---

예제

```python
text="Hello World"

new=text.replace("World","Python")

print(new)
```

결과

```python
Hello Python
```

---

교체 횟수 제한

```python
text.replace("world","Python",1)
```

앞에서부터 한 번만 교체한다.

---

# strip()

## 기능

양쪽 끝의 공백이나 특정 문자를 제거한다.

---

예제

```python
text="   Hello   "

print(text.strip())
```

결과

```python
Hello
```

---

특정 문자 제거

```python
text="!!!Hello!!!"

print(text.strip("!"))
```

결과

```python
Hello
```

> **중간 문자열은 절대 제거하지 않는다.**

---

# split()

## 기능

문자열을 나누어 리스트로 만든다.

---

공백 기준

```python
text="Hello Python"

print(text.split())
```

결과

```python
['Hello','Python']
```

---

쉼표 기준

```python
data="10,20,,30"

print(data.split(","))
```

결과

```python
['10','20','','30']
```

---

분할 횟수 제한

```python
path="User/admin/doc"

print(path.split("/",1))
```

결과

```python
['User','admin/doc']
```

---

# join()

## 기능

리스트를 하나의 문자열로 합친다.

문법이 가장 중요하다.

```python
'구분자'.join(리스트)
```

---

예제

```python
words=["Python","is","awesome"]

print(" ".join(words))
```

결과

```python
Python is awesome
```

---

```python
print("-".join(words))
```

결과

```python
Python-is-awesome
```

---

# 대소문자 변환 메서드

|메서드|설명|
|------|-----|
|capitalize()|첫 글자만 대문자|
|title()|단어마다 첫 글자 대문자|
|upper()|모두 대문자|
|lower()|모두 소문자|
|swapcase()|대소문자 뒤집기|

---

# 핵심 비교

## 문자열 메서드 특징

- 문자열은 불변 객체이다.
- 메서드를 호출해도 원본은 바뀌지 않는다.
- 결과를 사용하려면 반드시 변수에 저장해야 한다.

```python
text=text.upper()
```

---

# 반드시 기억할 것 ⭐

✅ 메서드는 `객체.메서드()` 형태로 호출한다.

✅ 문자열 메서드는 원본을 수정하지 않는다.

✅ `index()`는 없으면 에러

✅ `find()`는 없으면 -1

✅ `split()`은 문자열 → 리스트

✅ `join()`은 리스트 → 문자열