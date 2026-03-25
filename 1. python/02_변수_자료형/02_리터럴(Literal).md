	변수 또는 상수에 대입하는 '원시 데이터(raw data)'
	종류: 숫자형(Numeric), 문자열(String), 불리언(Boolean: True/False) 등

	- 기본 리터럴
```
# 1. 숫자형 (Numeric)
a = 0b1010  # 2진수 (Binary Literals)
b = 100     # 10진수 (Decimal Literal)
c = 0o310   # 8진수 (Octal Literal)
d = 0x12c   # 16진수 (Hexadecimal Literal)

float_1 = 10.5    # 실수 (Float Literal)
float_2 = 1.5e2   # 실수 지수표현 (Float Literal)

x = 3.14j         # 복소수 (Complex Literal)

# 2. 불리언 (Boolean) : 파이썬에서 True는 1, False는 0으로 계산됨
x = (1 == True)   # True
y = (1 == False)  # False
a = True + 4      # 1 + 4 = 5
b = False + 10    # 0 + 10 = 10

# 3. 문자열 (String)

strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string
with more than one line code."""
unicode = u"\u00dcnic\u00f6de" # 유니코드 문자열
raw_str = r"raw \n string" # 백슬래시(\)를 특수문자로 취급하지 않는 있는 그대로의 문자열
```

	- 특수 리터럴
		None : 값이 생성되지 않았음(아무것도 없음)을 지정하는 리터럴
```
# food에는 아무런 값도 없음을 지정
drink = "Available" 
food = None 
```

	- 리터럴 컬렉션
		여러 개의 데이터를 한 덩어리로 묶어서 표현하는 방법
		종류: 리스트(list), 튜플(tuple), 딕셔너리(dict), 셋(set)
```
# 1. List : 대괄호 [] 사용
fruits = ["apple", "mango", "orange"] 

# 2. Tuple : 소괄호 () 사용
numbers = (1, 2, 3)

# 3. Dictionary : 중괄호 {} 안에 '키:값' 형태로 저장
alphabets = {'a': 'apple', 'b': 'ball', 'c': 'cat'}

# 4. Set : 중괄호 {} 안에 값만 나열 (중복 허용 안 함)
vowels = {'a', 'e', 'i', 'o', 'u'}
```
