## 객체지향 프로그래밍(OOP)

### 객체지향 프로그래밍이란?

	- 프로그램을 객체 중심으로 설계하는 방식이다.
	- 코드 재사용성을 높이고 유지보수를 쉽게 만든다.
	- Python은 객체지향을 지원하는 다중 패러다임 언어이다.

### 핵심 개념

```text
Class
Object
Method
Inheritance
Encapsulation
Polymorphism
```

### Class

	- 객체를 만들기 위한 설계도이다.

### Object

	- 클래스를 기반으로 실제 생성된 대상이다.

### Method

	- 클래스 내부에 정의된 함수이다.
	- 객체의 동작을 정의한다.

### 클래스 기본 예제

```python
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)


kim = Human("kim", 10)

print(kim.sing("Happy"))
print(kim.dance())
```

### 생성자 `__init__`

	- 객체가 생성될 때 자동으로 실행된다.
	- 객체의 초기값을 설정할 때 사용한다.

```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Kim")
print(p.name)
```

### self

	- 현재 객체 자기 자신을 의미한다.
	- 인스턴스 변수와 메서드에 접근할 때 사용한다.

### 상속(Inheritance)

	- 기존 클래스의 기능을 물려받아 새로운 클래스를 만드는 방식이다.
	- 코드 재사용에 유리하다.

```python
class Animal:
    def eat(self):
        print("먹는다")

class Dog(Animal):
    def bark(self):
        print("멍멍")


dog = Dog()
dog.eat()
dog.bark()
```

### 캡슐화(Encapsulation)

	- 데이터와 기능을 하나로 묶고, 외부 접근을 제한하는 개념이다.
	- 직접적인 데이터 수정을 막는 데 사용한다.

	예제

```python
class Account:
    def __init__(self):
        self.__balance = 0

    def deposit(self, money):
        self.__balance += money

    def get_balance(self):
        return self.__balance


acc = Account()
acc.deposit(10000)
print(acc.get_balance())
```

### 다형성(Polymorphism)

	- 서로 다른 객체가 같은 메서드 이름을 사용해도 각자 다르게 동작하는 것이다.

```python
class Parrot:
    def fly(self):
        print("Parrot can fly")

class Penguin:
    def fly(self):
        print("Penguin can't fly")


def flying_test(bird):
    bird.fly()


parrot = Parrot()
penguin = Penguin()

flying_test(parrot)
flying_test(penguin)
```

### 시험 포인트

	Q. 객체를 만들기 위한 설계도는?
	정답: 클래스

	Q. 클래스 내부에 정의된 함수는?
	정답: 메서드

	Q. 기존 클래스 기능을 물려받는 개념은?
	정답: 상속

---
