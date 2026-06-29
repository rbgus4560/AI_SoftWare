## Tuple

### Tuple이란?

	- List와 대부분 비슷하지만 내부 값을 변경할 수 없는 자료형이다.
	- 괄호 없이도 선언 가능하지만 쉼표가 중요하다.

### Tuple 생성

```python
my_tuple = (1, 2, 3)
print(my_tuple)
```

### 괄호 없이 생성

```python
my_tuple = 1, 2, 3
print(my_tuple)
```

### 요소 하나짜리 Tuple

```python
single_tuple = (1,)
print(type(single_tuple))
```

	주의

```python
not_tuple = (1)
print(type(not_tuple))
```

	결과

```text
<class 'int'>
```

### Tuple 인덱싱

```python
my_tuple = (10, 20, 30)
print(my_tuple[0])
print(my_tuple[-1])
```

### Tuple 슬라이싱

```python
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[1:4])
```

### Tuple 수정 불가

```python
my_tuple = (1, 2, 3)
my_tuple[0] = 100
```

	오류 이유

```text
Tuple은 immutable 자료형이다.
```

### 내부 요소가 List인 경우

```python
my_tuple = (1, [2, 3], 4)
my_tuple[1][0] = 100
print(my_tuple)
```

	핵심

```text
Tuple 자체는 변경 불가이지만, 내부에 들어 있는 mutable 객체는 변경될 수 있다.
```

### Tuple 재할당

```python
my_tuple = (1, 2, 3)
my_tuple = (4, 5, 6)
print(my_tuple)
```

### 시험 포인트

	Q. Tuple과 List의 가장 큰 차이는?
	정답: Tuple은 생성 후 내부 요소 변경이 불가능하다.

---
