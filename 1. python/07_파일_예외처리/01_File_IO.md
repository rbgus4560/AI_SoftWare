## File I/O

### 파일 입출력이란?

	- 프로그램에서 파일을 읽거나 쓰는 작업이다.
	- 텍스트 파일, 로그 파일, CSV 파일 처리 등에 사용한다.

### 파일 열기와 닫기

```python
f = open("test.txt", "r")
f.close()
```

### 파일 모드

| 모드 | 의미 |
|---|---|
| r | 읽기 모드 |
| w | 쓰기 모드, 기존 내용 삭제 |
| a | 추가 모드, 기존 내용 뒤에 추가 |
| x | 새 파일 생성, 이미 있으면 오류 |
| t | 텍스트 모드 |
| b | 바이너리 모드 |
| + | 읽기/쓰기 모두 가능 |

### 파일 쓰기

```python
f = open("test.txt", "w")
f.write("Hello Python")
f.close()
```

### 파일 읽기

```python
f = open("test.txt", "r")
data = f.read()
f.close()

print(data)
```

### with 사용

	- 파일을 자동으로 닫아준다.
	- 실무에서는 이 방식을 권장한다.

```python
with open("test.txt", "w") as f:
    f.write("Hello Python")

with open("test.txt", "r") as f:
    data = f.read()

print(data)
```

### 한 줄씩 읽기

	for문 사용

```python
with open("test.txt", "r") as f:
    for line in f:
        print(line)
```

	readline()

```python
with open("test.txt", "r") as f:
    line = f.readline()
    print(line)
```

	readlines()

```python
with open("test.txt", "r") as f:
    lines = f.readlines()
    print(lines)
```

### 주요 파일 메서드

| 메서드 | 의미 |
|---|---|
| close() | 파일 닫기 |
| read() | 전체 읽기 |
| readline() | 한 줄 읽기 |
| readlines() | 모든 줄을 리스트로 읽기 |
| write() | 문자열 쓰기 |
| writelines() | 문자열 리스트 쓰기 |
| seek() | 파일 포인터 위치 이동 |
| tell() | 현재 파일 포인터 위치 반환 |
| flush() | 버퍼 내용 즉시 기록 |

### 폴더/파일 관리

	- `os` 모듈을 사용한다.

```python
import os

print(os.getcwd())      # 현재 작업 폴더
print(os.listdir())     # 현재 폴더 파일 목록
```

### 작업 폴더 변경

```python
import os

os.chdir("./data")
```

### 폴더 생성

```python
import os

os.mkdir("new_folder")
os.makedirs("parent/child")
```

### 이름 변경

```python
import os

os.rename("old.txt", "new.txt")
```

### 시험 포인트

	Q. 파일을 자동으로 닫아주는 구문은?
	정답: `with open(...) as f:`

	Q. 기존 내용 뒤에 추가하는 파일 모드는?
	정답: `a`

	Q. 전체 내용을 읽는 메서드는?
	정답: `read()`

---
