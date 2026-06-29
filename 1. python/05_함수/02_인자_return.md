## 인자와 return

### 함수 인자(arguments)

	- 함수를 호출할 때 전달하는 값이다.
	- 선언된 인자 개수와 호출 시 전달하는 인자 개수가 맞지 않으면 오류가 발생한다.

	예제

```python
def greet(name, msg):
    print("Hello", name + ",", msg)


greet("Monica", "Good morning")
```

### 기본값 인자(Default Arguments)

	- 함수 정의 시 인자의 기본값을 지정할 수 있다.

```python
def greet(name, msg="Good morning"):
    print("Hello", name + ",", msg)


greet("Kim")
greet("Park", "How are you?")
```

	주의사항

```text
기본값 인자 뒤에 오는 인자는 모두 기본값이 있어야 한다.
```

### 키워드 인자(Keyword Arguments)

	- 인자 이름을 직접 지정해서 값을 전달한다.

```python
def greet(name, msg):
    print("Hello", name + ",", msg)


greet(msg="Good morning", name="Kim")
```

	주의사항

```text
키워드 인자 뒤에 위치 인자를 사용하면 오류가 발생할 수 있다.
```

### 임의 개수 인자(Arbitrary Arguments)

	- 인자 개수를 미리 정하지 않을 때 사용한다.
	- `*args` 형태로 작성한다.
	- 내부적으로 tuple처럼 처리된다.

```python
def greet(*names):
    for name in names:
        print("Hello", name)


greet("Kim", "Lee", "Park")
```
