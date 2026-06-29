## Dictionary

### Dictionary란?

	- Key와 Value의 쌍으로 데이터를 저장하는 자료형이다.
	- Key를 이용해 Value에 접근한다.
	- 데이터 검색에 유리하다.

### Dictionary 생성

```python
my_dict = {}
print(type(my_dict))
```

```python
my_dict = {1: "apple", 2: "ball"}
print(my_dict)
```

```python
my_dict = {"name": "Jack", "age": 26}
print(my_dict)
```

### 값 접근

```python
my_dict = {"name": "Jack", "age": 26}

print(my_dict["name"])
print(my_dict.get("age"))
```

### 없는 Key 접근 차이

```python
my_dict = {"name": "Jack"}

print(my_dict.get("age"))
```

	결과

```text
None
```

```python
print(my_dict["age"])
```

	오류 이유

```text
없는 Key를 대괄호로 접근하면 KeyError 발생
```

### 값 변경

```python
my_dict = {"name": "Jack", "age": 26}
my_dict["age"] = 27
print(my_dict)
```

### 값 추가

```python
my_dict["address"] = "Seoul"
print(my_dict)
```

### 값 삭제

	pop()

```python
squares = {1: 1, 2: 4, 3: 9, 4: 16}
print(squares.pop(4))
print(squares)
```

	popitem()

```python
squares = {1: 1, 2: 4, 3: 9}
print(squares.popitem())
print(squares)
```

	clear()

```python
squares = {1: 1, 2: 4}
squares.clear()
print(squares)
```

	del

```python
squares = {1: 1, 2: 4}
del squares
```

### Dictionary Comprehension

```python
squares = {x: x * x for x in range(6)}
print(squares)
```

	실행 결과

```text
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### Dictionary 주요 메서드

| 메서드 | 의미 |
|---|---|
| clear() | 전체 삭제 |
| copy() | 복사 |
| fromkeys() | 지정한 Key들로 딕셔너리 생성 |
| get() | Key에 해당하는 Value 반환 |
| items() | Key-Value 쌍 반환 |
| keys() | Key 목록 반환 |
| values() | Value 목록 반환 |
| pop() | 특정 Key 삭제 후 Value 반환 |
| popitem() | 마지막 Key-Value 쌍 삭제 |
| update() | 다른 딕셔너리 내용 추가/수정 |

### Dictionary 내장 함수

| 함수 | 의미 |
|---|---|
| all() | 모든 Key가 참이면 True |
| any() | 하나라도 참이면 True |
| len() | Key 개수 반환 |
| sorted() | Key를 정렬한 리스트 반환 |

### 시험 포인트

	Q. Dictionary에서 Key 목록을 얻는 메서드는?
	정답: `keys()`

	Q. 없는 Key에 안전하게 접근할 때 사용하는 메서드는?
	정답: `get()`

---
