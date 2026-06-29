## List 심화

### List란?

	- 여러 요소를 한 번에 저장할 수 있는 자료형이다.
	- 각 요소는 순서대로 접근할 수 있다.
	- 인덱스는 0부터 시작한다.
	- 음수 인덱스를 사용할 수 있다.

### List 생성

```python
my_list = [1, 2, 3, 4]
empty_list = []
```

### 여러 자료형 혼합

```python
mixed = [1, "Python", 3.14, True]
print(mixed)
```

### 인덱싱

```python
my_list = [10, 20, 30, 40]

print(my_list[0])
print(my_list[-1])
```

### 슬라이싱

```python
my_list = [10, 20, 30, 40, 50]

print(my_list[1:4])
print(my_list[:3])
print(my_list[2:])
```

### 요소 변경

```python
my_list = [1, 2, 3]
my_list[0] = 100
print(my_list)
```

### 요소 추가

	append()

```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
```

	extend()

```python
my_list = [1, 2]
my_list.extend([3, 4])
print(my_list)
```

	insert()

```python
my_list = [1, 3]
my_list.insert(1, 2)
print(my_list)
```

### 요소 삭제

	del

```python
my_list = [1, 2, 3, 4]
del my_list[0]
print(my_list)
```

	remove()

```python
my_list = [1, 2, 3]
my_list.remove(2)
print(my_list)
```

	pop()

```python
my_list = [1, 2, 3]
item = my_list.pop()
print(item)
print(my_list)
```

	clear()

```python
my_list = [1, 2, 3]
my_list.clear()
print(my_list)
```

### List 주요 메서드

| 메서드 | 의미 |
|---|---|
| append() | 끝에 요소 추가 |
| extend() | 여러 요소 추가 |
| insert() | 특정 위치에 추가 |
| remove() | 특정 값 삭제 |
| pop() | 요소 꺼내고 삭제 |
| clear() | 전체 삭제 |
| index() | 값의 인덱스 반환 |
| count() | 값의 개수 반환 |
| sort() | 정렬 |
| reverse() | 순서 뒤집기 |
| copy() | 복사 |

### List Comprehension

	- 반복문을 이용해 리스트를 간결하게 생성하는 방법이다.

	일반 방식

```python
pow2 = []
for x in range(10):
    pow2.append(2 ** x)

print(pow2)
```

	List Comprehension 방식

```python
pow2 = [2 ** x for x in range(10)]
print(pow2)
```

### 조건 포함

```python
odd = [x for x in range(20) if x % 2 == 1]
print(odd)
```

### 여러 조건 포함

```python
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)
```

### 중첩 리스트 처리

```python
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]
transposed = []

for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)
```

### 시험 포인트

	Q. 리스트 끝에 요소 하나를 추가하는 메서드는?
	정답: `append()`

	Q. 리스트의 모든 요소를 제거하는 메서드는?
	정답: `clear()`

	Q. 리스트 컴프리헨션은 왜 사용하는가?
	정답: 반복문을 간결하게 작성하기 위해 사용한다.

---
