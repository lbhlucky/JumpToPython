# 함수
# - 반복되는 부분이 있을 경우 '반복적으로 사양되는 가치 있는  부분'을 한 뭉치로 묶어서
#   어떤 입력값을 주었을 때 어떤 결괏값을 돌려준다.
#   단, 입/출력이 없는 경우도 있다.

# 기본 구조
# def 함수명(매개변수):
#   실행문

# 일반적인 함수

# def 함수명(매개변수)
#   실행문
#   return 결괏값

def sum(a, b):
    result = a+b
    return result

# 결괏값을 받을 변수 = 함수명(입력인수1, 입력인수2, 입력인수n)
print(sum(1,2))

# 입력값이 없는 함수
def say():
    return "hello"
#결괏값을 받을 변수 = 함수명()
hello = say()
print(hello)

# 결괏값이 없는 함수
def add(a, b):
    print("%d와 %d의 합은 %d입니다." %(a, b, (a+b)))

# 함수명(입력인수1, 입력인수2, 입력인수n)
add(1,3)

# 입력값과 결괏값이 없는 함수
def hi():
    print('hi')

# 함수명()
hi()

# 여러 개의 입력값을 받는 함수 만들기
# *매개변수 사용 : 일반적으로 *args 사용
# def 함수명(*매개변수):
#   실행문

# 키워드 파라미터 : **매개변수사용

def sum_total(*args):
    sum = 0
    for i in args:
        sum += i
    print("입력 받은 수의 총합은 %d 입니다." %sum)

sum_total(1,2,3)

# 함수의 결괏값은 항상 하나이다.

# 매개변수에 초기값 미리 설정하기
# 함수의 마지막 매개변수가 bool형이고 미리 설정되어있을 경우 생략가능
def intro_myself(name, old, gender = True):
    print("나의 이름은 %s 입니다." %name)
    print("나는 %d 살 입니다." %old)
    if gender:
        print("나는 남자입니다.")
    else:
        print("나는 여자입니다.")

intro_myself("홍길동", 30)

# 사용자 입력 출력
# 사용자 입력
# input() - 사용자에게 프롬프트를 통해 입력받을 때 사용, 알고리즘 풀이시 자주 사용

# print 자세히 알기
# 큰따옴표(")로 둘러싸인 문자열은 + 연산과 동일
# 문자열 띄어쓰기는 콤마(,)로 한다.
# 한 줄에 결괏값 출력 : end=''

# 파일 읽고 쓰기
# 파일 객체 = open(파일명, 모드)
# 파일 열기 모드
# w : 쓰기 모드
# r : 읽기 모드
# a : 추가 모드 - 파일의 마지막에 새로운 내용 추가
# 작업이 끝난 후에는 반드시 close()를 통해 닫아 주어야한다.
f = open('foo.txt','w')
f.write("The foo")
f.close()

# with문과 함께 사용하기
# - with : 파일을 열고 닫는 것을 자동으로 처리해주는 기능
# with open(파일명, 모드) as 파일 객체
with open("foo.txt",'r') as f:
    print(f.read())

