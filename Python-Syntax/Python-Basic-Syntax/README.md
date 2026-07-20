# Python Syntax Basic

> 2026.07.20 Python 기본 문법 정리

---

## 1. 변수와 할당

파이썬에서 변수는 값을 저장하는 공간이다.

```python
number = 10
double = 2 * number

print(double)  # 20
```

변수의 값이 변경되어도 기존에 계산된 변수는 자동으로 변경되지 않는다.

```python
number = 5

print(double)  # 20

# double이 10이 되려면 다시 할당 필요
double = 2 * number

print(double)  # 10
```

---

# 2. Data Type

파이썬의 주요 데이터 타입

| 종류 | 자료형 | 설명 |
|:---:|:---:|:---|
| 숫자 | `int` | 정수 |
| 숫자 | `float` | 실수 |
| 숫자 | `complex` | 복소수 |
| 문자 | `str` | 문자열 |
| 시퀀스 | `list` | 변경 가능한 순서형 데이터 |
| 시퀀스 | `tuple` | 변경 불가능한 순서형 데이터 |
| 시퀀스 | `range` | 연속된 숫자 생성 |
| 비시퀀스 | `set` | 중복 없는 집합 |
| 비시퀀스 | `dict` | key-value 구조 |
| 기타 | `boolean` | True / False |
| 기타 | `None` | 값이 없음을 표현 |
| 기타 | `function` | 함수 객체 |

---

# 3. 연산자 우선순위

파이썬 연산자는 아래 순서대로 실행된다.

```
1. 지수 (**)
2. 음수 부호 (-)
3. 곱셈, 나눗셈, 나머지 (* / %)
4. 덧셈, 뺄셈 (+ -)
```

예시:

```python
print(-2**4)
```

실행 순서:

```
1. 2**4 = 16
2. - 부호 적용
3. 결과 = -16
```

출력:

```
-16
```

---

# 4. 문자열(String)

## 문자열 내 따옴표 출력

### 1) 서로 다른 따옴표 사용

```python
print("안녕 'Python'")
```

출력:

```
안녕 'Python'
```

---

### 2) Escape Sequence 사용

특수 문자를 표현할 때 `\` 사용

```python
print('I\'m Python')
```

출력:

```
I'm Python
```

---

# 5. 문자열의 특징

문자열도 **시퀀스(sequence)** 자료형이므로 리스트와 비슷한 기능을 사용할 수 있다.

## 1) 인덱싱(Indexing)

특정 위치의 문자 접근

```python
my_str = "Python"

print(my_str[1])
```

출력:

```
y
```

---

## 2) 슬라이싱(Slicing)

문자열 일부 추출

```python
my_str = "Python"

print(my_str[1:4])
```

출력:

```
yth
```

형식:

```python
문자열[시작:끝:증감]
```

---

## 3) 길이 확인

```python
my_str = "Python"

print(len(my_str))
```

출력:

```
6
```

---

## 4) 반복

```python
my_str = "Python"

for char in my_str:
    print(char)
```

출력:

```
P
y
t
h
o
n
```

---

# 6. 음수 인덱스

파이썬은 음수 인덱스를 지원한다.

마지막 요소는 `-1`로 접근한다.

```python
my_str = "Python"

print(my_str[-1])
```

출력:

```
n
```

인덱스 구조:

```
 P   y   t   h   o   n
 0   1   2   3   4   5
-6  -5  -4  -3  -2  -1
```

---

# 7. 문자열 수정 불가능 (Immutable)

문자열은 생성 후 특정 문자를 직접 변경할 수 없다.

```python
text = "Python"

text[0] = "J"
```

오류 발생:

```
TypeError
```

변경하려면 새로운 문자열을 만들어 재할당해야 한다.

```python
text = "Jython"
```

---

# 8. 진법 표현

파이썬에서는 접두사를 통해 다양한 진법 표현 가능

| 진법 | 표현 | 예시 | 10진수 변환 |
|---|---|---|---|
| 2진수 | `0b` | `0b10` | 2 |
| 8진수 | `0o` | `0o30` | 24 |
| 16진수 | `0x` | `0x10` | 16 |

예:

```python
print(0b10)
print(0o30)
print(0x10)
```

출력:

```
2
24
16
```

---

# 9. 부동소수점 오차

컴퓨터는 숫자를 **2진수**로 저장한다.

하지만 일부 소수는 2진수로 정확하게 표현할 수 없어 오차가 발생한다.

예:

```python
print(3.2 - 3.1)
```

결과:

```
0.10000000000000009
```

---

## Decimal 사용

정확한 소수 계산이 필요한 경우 `decimal` 모듈 사용

```python
from decimal import Decimal

a = Decimal('3.2') - Decimal('3.1')

print(a)
```

출력:

```
0.1
```

> Decimal 사용 시 문자열 형태로 값을 전달하는 것이 좋다.