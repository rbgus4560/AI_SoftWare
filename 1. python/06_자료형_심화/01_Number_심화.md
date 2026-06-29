## Number 자료형 심화

### Number 자료형 종류

```text
int
float
complex
```

### type()

	- 값의 자료형을 확인한다.

```python
print(type(10))
print(type(3.14))
print(type(1 + 2j))
```

### isinstance()

	- 값이 특정 클래스에 속하는지 확인한다.

```python
print(isinstance(10, int))
print(isinstance(3.14, float))
```

### float의 한계

	- 실수는 내부적으로 정확히 표현되지 않을 수 있다.

```python
print(0.1 + 0.2)
```

	예상과 다른 결과

```text
0.30000000000000004
```

### Decimal

	- 더 정확한 소수 계산이 필요할 때 사용한다.
	- 일반 float보다 느릴 수 있다.

```python
from decimal import Decimal

print(Decimal("0.1") + Decimal("0.2"))
```

	실행 결과

```text
0.3
```

### Fraction

	- 분수 형태의 계산을 지원한다.

```python
from fractions import Fraction

print(Fraction(1, 3))
print(Fraction(1, 3) + Fraction(1, 3))
```

### math 모듈

	- 수학 계산을 위한 함수들을 제공한다.

	자주 사용하는 함수

| 함수 | 의미 |
|---|---|
| ceil(x) | x보다 크거나 같은 가장 작은 정수 |
| floor(x) | x보다 작거나 같은 가장 큰 정수 |
| sqrt(x) | 제곱근 |
| factorial(x) | 팩토리얼 |
| fabs(x) | 절댓값 |
| pow(x, y) | 거듭제곱 |
| sin(x), cos(x), tan(x) | 삼각함수 |

	예제

```python
import math

print(math.sqrt(16))
print(math.factorial(5))
print(math.ceil(3.2))
print(math.floor(3.8))
```

### random 모듈

	- 난수 생성 기능을 제공한다.

	자주 사용하는 함수

| 함수 | 의미 |
|---|---|
| random() | 0 이상 1 미만의 실수 난수 |
| randint(a, b) | a부터 b까지의 정수 난수 |
| randrange(start, stop, step) | 범위 내 정수 난수 |
| choice(seq) | 시퀀스에서 하나 선택 |
| shuffle(seq) | 순서 섞기 |
| sample(population, k) | k개 샘플 추출 |
| seed() | 난수 기준값 설정 |

	예제

```python
import random

print(random.random())
print(random.randint(1, 10))
print(random.choice(["apple", "banana", "orange"]))
```

### 시험 포인트

	Q. 정확한 소수 계산이 필요할 때 사용하는 모듈은?
	정답: `decimal`

	Q. 난수 생성을 위한 모듈은?
	정답: `random`

---
