# Python Collection Types & Type Conversion

## List (리스트)

리스트는 여러 개의 값을 순서대로 저장하는 **변경 가능한(mutable) 시퀀스 자료형**이다.

- 원소는 쉼표(`,`)로 구분한다.
- 시퀀스 자료형이므로 문자열처럼 인덱싱, 슬라이싱, 길이 확인, 반복 등 공통 기능을 사용할 수 있다.

### List 주요 기능

- 인덱싱 : 특정 위치의 값 접근
- 슬라이싱 : 범위에 해당하는 값 추출
- 길이 확인 : `len()` 사용
- 반복 : `for`문 사용 가능

```python
lst = [1, 2, 3, 'Python']

print(lst[0])      # 1
print(lst[1:3])    # [2, 3]
print(len(lst))    # 4
```

---

## 중첩 리스트 (Nested List)

중첩 리스트는 리스트 내부에 다른 리스트를 값으로 가지는 형태이다.

```python
lst = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]

print(len(lst))       # 5
print(lst[4][1])      # world
print(lst[-1][1][0])  # w
```

리스트는 인덱스를 활용하여 값을 수정할 수 있다.

```python
lst = [1, 2, 3]

lst[0] = 10

print(lst)

# [10, 2, 3]
```

여러 값을 한 번에 변경하는 것도 가능하다.

```python
lst[1:3] = [20, 30]

print(lst)

# [1, 20, 30]
```

---

## Tuple (튜플)

튜플은 여러 개의 값을 순서대로 저장하는 **변경 불가능한(immutable) 시퀀스 자료형**이다.

특징:

- 소괄호 `()`를 사용한다.
- 모든 종류의 데이터를 저장할 수 있다.
- 생성 후 값을 수정할 수 없다.

```python
tuple1 = ()

tuple2 = (1,)

tuple3 = (1, 'hello', 3.14, True)
```

단일 요소 튜플을 생성할 때는 반드시 후행 쉼표(`,`)가 필요하다.

```python
tuple1 = (1,)  # 튜플
tuple2 = (1)   # 정수
```

또한 소괄호 없이도 생성 가능하다.

```python
tuple3 = 1, 'hello', 3.14, True
```

튜플 역시 시퀀스 자료형이므로 인덱싱, 슬라이싱, 길이 확인, 반복 등의 기능을 사용할 수 있다.

---

## Range (범위)

range는 연속된 정수를 생성하는 **변경 불가능한(immutable) 시퀀스 자료형**이다.

형식:

```python
range(start, stop, step)
```

- `start` : 시작 값 (포함)
- `stop` : 종료 값 (미포함)
- `step` : 증가 값

예시:

```python
range(1, 5)

# 1, 2, 3, 4 생성
```

주의:

> stop 값은 시퀀스에 포함되지 않는다.

---

## Dictionary (딕셔너리)

딕셔너리는 **key-value 쌍으로 이루어진 변경 가능한 자료형**이다.

특징:

- 중괄호 `{}`를 사용한다.
- 하나의 값은 key와 value의 쌍으로 구성된다.
- key를 사용하여 value에 접근한다.
- key는 중복될 수 없다.
- key는 변경 불가능한 자료형만 사용할 수 있다.

```python
my_dict = {
    'name': '서희수',
    'age': 29
}

print(my_dict['name'])

# 서희수
```

### Dictionary 값 추가

새로운 key를 지정하면 값을 추가할 수 있다.

```python
my_dict['banana'] = 50

print(my_dict)

# {'name': '서희수', 'age': 29, 'banana': 50}
```

### Dictionary Key 특징

key는 중복될 수 없다.

```python
my_dict = {
    'name': 'Kim',
    'name': 'Lee'
}

print(my_dict)

# {'name': 'Lee'}
```

같은 key가 존재하면 마지막 값으로 덮어쓴다.

또한 key는 변경 불가능한 자료형만 사용할 수 있다.

가능:

```python
my_dict = {
    1: 'number',
    'a': 'string',
    (1, 2): 'tuple'
}
```

불가능:

```python
my_dict = {
    [1, 2]: 'list'
}
```

리스트와 딕셔너리는 변경 가능한 자료형이므로 key로 사용할 수 없다.

---

## Set (세트)

세트는 **순서가 없고 중복을 허용하지 않는 변경 가능한 자료형**이다.

특징:

- 중괄호 `{}`를 사용한다.
- 중복 값을 저장하지 않는다.
- 순서가 없으므로 인덱싱이 불가능하다.

```python
my_set = {1, 2, 2, 3, 3}

print(my_set)

# {1, 2, 3}
```

---

## Type Conversion (형변환)

### 암시적 형변환

파이썬이 자동으로 자료형을 변환하는 경우이다.

주로 정수와 실수 연산에서 발생한다.

```python
print(3 + 5.0)

# 8.0

print(True + 3)

# 4

print(False + True)

# 1
```

Boolean 값은 연산에서 다음과 같이 처리된다.

```python
True == 1
False == 0
```

---

### 명시적 형변환

개발자가 직접 변환 함수를 사용하여 자료형을 변경하는 방식이다.

문자열 → 정수

```python
print(int('345'))

# 345
```

실수 → 정수

```python
print(int(3.5))

# 3
```

소수점 이하 값은 버려진다.

정수 → 문자열

```python
print(str(1) + '등')

# 1등
```

문자열과 숫자는 직접 연결할 수 없으므로 `str()`을 이용해 변환한다.

---

## Python Collection Type 정리

| 자료형 | 특징 | 변경 가능 여부 |
| --- | --- | --- |
| List | 순서 있음, 중복 허용 | Mutable |
| Tuple | 순서 있음, 중복 허용 | Immutable |
| Range | 연속된 정수 생성 | Immutable |
| Dictionary | Key-Value 구조 | Mutable |
| Set | 순서 없음, 중복 제거 | Mutable |