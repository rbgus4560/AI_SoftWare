## Class 심화

### 클래스 생성 방법

```python
class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)
```

### 클래스 속성 삭제

```python
class MyClass:
    x = 5

p1 = MyClass()
del p1
```

### 속성 삭제

```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Kim")
del p.name
```

### 메모리와 Garbage Collection

	- `del`은 이름과 객체의 연결을 끊는다.
	- 실제 메모리 해제는 garbage collection에 의해 나중에 처리될 수 있다.

### 상속 확인

	isinstance()

```python
class Animal:
    pass

class Dog(Animal):
    pass


dog = Dog()
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
```

	issubclass()

```python
print(issubclass(Dog, Animal))
```

### 상속 예제

```python
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def input_sides(self):
        self.sides = [float(input("Enter side " + str(i + 1) + ": ")) for i in range(self.n)]

    def display_sides(self):
        for i in range(self.n):
            print("Side", i + 1, "is", self.sides[i])


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

    def find_area(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print("The area of the triangle is %0.2f" % area)
```

### 다중 상속(Multiple Inheritance)

	- 하나의 클래스가 여러 부모 클래스를 상속받는 것이다.

```python
class Base1:
    pass

class Base2:
    pass

class MultiDerived(Base1, Base2):
    pass
```

### MRO(Method Resolution Order)

	- 다중 상속에서 메서드를 찾는 순서이다.
	- `__mro__` 또는 `mro()`로 확인한다.

```python
print(MultiDerived.__mro__)
print(MultiDerived.mro())
```

### Overloading

	- Python에서는 연산자 오버로딩을 특수 메서드로 구현한다.
	- 특수 메서드는 보통 `__이름__` 형태이다.

### 특수 함수 예제

```python
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


p1 = Point(1, 2)
p2 = Point(2, 3)

print(p1 + p2)
```

### 주요 연산자와 특수 메서드

| 연산자 | 내부 호출 메서드 |
|---|---|
| p1 + p2 | `p1.__add__(p2)` |
| p1 - p2 | `p1.__sub__(p2)` |
| p1 * p2 | `p1.__mul__(p2)` |
| p1 ** p2 | `p1.__pow__(p2)` |
| p1 / p2 | `p1.__truediv__(p2)` |
| p1 // p2 | `p1.__floordiv__(p2)` |
| p1 % p2 | `p1.__mod__(p2)` |
| p1 < p2 | `p1.__lt__(p2)` |
| p1 <= p2 | `p1.__le__(p2)` |
| p1 == p2 | `p1.__eq__(p2)` |
| p1 != p2 | `p1.__ne__(p2)` |
| p1 > p2 | `p1.__gt__(p2)` |
| p1 >= p2 | `p1.__ge__(p2)` |

### 시험 포인트

	Q. 클래스의 생성자 메서드는?
	정답: `__init__`

	Q. 객체를 문자열로 출력할 때 사용하는 특수 메서드는?
	정답: `__str__`

	Q. `+` 연산자 오버로딩에 사용하는 특수 메서드는?
	정답: `__add__`

---
