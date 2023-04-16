# 클래스 : 반복되는 변수 & 메서드(함수)를 미리 정해놓는 틀(설계도)
# - 프로그램 작성 시 꼭 필요한 것은 아님.
# - 첫글자는 대문자로 작성하는 것이 관례적


# 클래스(class) : 똑같은 무언가를 계속해서 만들어 낼 수 있는 설계 도면(과자틀)
# 객체(object) : 클래스로 만들 피조물(과자틀을 사용해 만든 과자)
# 인스턴스(instance) : 클래스로 만든 객체

# 사칙 연산 클래스 만들기
# 1. 클래스를 어떻게 만들 것인지 구상하기
# 2. 클래스 구조 만들기
# 3. 객체에 숫자를 지정할 수 있게 만들기
# 4. 더하기 기능 만들기
# 5. 빼기, 곱하기, 나누기 기능 만들기

# 생성자(Constructor) : 객체가 생성될 때 자동으로 호출되는 메서드
#  __init__ 를 사용

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def sum(self):
        result = self.num1 + self.num2
        return result
    def sub(self):
        result = self.num1 - self.num2
        return result
    def mul(self):
        result = self.num1 * self.num2
        return result
    def div(self):
        result = self.num1 / self.num2
        return result
    
cal = Calculator(3,2)

print(cal.sum())    # 3 + 2 = 5     5 출력
print(cal.sub())    # 3 - 2 = 1     1 출력 
print(cal.mul())    # 3 * 2 = 6     6 출력
print(cal.div())    # 3 / 2 = 1.5   1.5 출력

# 클래스의 상속(Inheritance) : 클래스를 만들 때 다른 클래스의 기능을 물려받을  수 있게 만드는 것
# - 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용
# class 상속 받을 클래스 이름(상속할 클래스 이름)

# 메서드(함수) 오버라이딩 : 부모클래스(상속한 클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것
# --> 메서드 오버라이딩을 하면 부모클래스의 메서드 대신 오버라이딩한(자식클래스) 메서드가 호출된다.
#     (자식 이기는 부모 없다.ㅋ)

class safeCalculator(Calculator):
    def div(self):
        if self.num2 == 0:
            return 0
        else:
            return self.num1 / self.num2

cal2 = safeCalculator(4,0)
print(cal.div())
print(cal2.div())

# 클래스 변수 : 클래스 안에 함수를 선언하는 것과 마찬가지로 클래스 안에 변수를 선언하는 것
# -> 클래스로 만든 모든 객체에 공유된다.

# 모듈 : 미리 만들어 놓은 .py 파일(변수, 함수, 클래스)

# import
# - 이미 만들어 놓은 파이썬 모듈을 사용할 수 있게 해주는 명령어
# 1. import 모듈이름 
# 2. from 모듈이름 import 모듈함수
# '*' : 모든것

#if __name__=="__main__"이라는 조건문을 넣어주고 그 아래는 직접 실행시켰을 때만 실행되길 원하는 코드들을 넣어주는 것
# __name__ 변수란?
# -> 파이썬이 내부적으로 사용하는 특별한 변수
# __all__
# -> * 햇을 때 어떤 것까지 불러올지
# 패키지 : 모듈을 여러개 모아놓은 것

# __init__.py 의 용도
# - 해당 디렉터리가 패키지의 일부임을 알려주는 역할
#   참고) python3.3 버전부터는 __init__.py 파일이 없어도 패키지로 인식하지만 하위 버전 호환을 위해 생성하는 것이 안전

# 예외 처리 
# 오류 예외 처리 기법
# 1. try, except문
# try:
#   실행문
# except [발생 오류[as 오류메세지변수]]:
#   실행문

# 2. try...finally 문
# finally절 : 수행 도중 예외 발생 여부에 상관없이 항상 수행
#             - 사용한 리소스를 close 해야 할 때 주로 사용

# 오류 회피하기 : pass 사용

# 오류 일부러 발생시키기 : raise 사용

# 예외 만들기

# 내장함수
# abs(x) : 절댓값 리턴
# all(x) : 반복 가능한 자료형 x를 받아 모두 참이면 True, 아니면 False
# any(x) : 반복 가능한 자료형 x를 받아 하나라도 참이면 True, 모두 거짓일 때만 False
# chr(i) : 아스키 코드를 입력 받아 문자 출력
# dir : 객체가 가지고 있는 변수나 함수 보여줌
# divmod(x, y) : x를 y로 나눈 몫과 나머지를 튜플 형으로 리턴 (몫, 나머지)
# enumerate : 순서가 있는 자료형을 입력 받아 인덱스를 포함한 값을 리턴
# eval : 실행 가능한 문자열을 받아 결괏값 리턴

# * filter : 첫번째 인수로 함수이름, 두번째 인수로 반복 가능한 자료형을 받아, 두번째 인수가 첫번째 인수에 입력됬을 때
#          반환 값이 참이 것만 묶어서 리턴

# hex : 정수 값을 입력 받아 16진수로 변환 후 리턴
# id : 객체 고유 주소 리턴
# * input : 사용자 입력 받는 함수
# int : 문자열 형태의 변수를 정수형으로 변환 후 리턴
# * len : 입력값의 길이 리턴

# 라이브러리 : 파이썬 설치시 자동으로 설치됨, 모듈을 모아놓은 것(?)

# sys : 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈

# sys.argv : 명령행에서 인수 전달하기 
import sys
# print(sys.argv)

# sys.exit : 강제로 스크립트 종료하기
# sys.exit()

# sys.path : 자신이 만든 모듈 불러와 사용하기

# pickle : 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈

# os : 환경 변수나 디렉터리, 파일 등의 os 자원을 제어할 수 있게 해주는 모듈
#os.environ 내 시스템의 환경 변수 값을 알고 싶을 때 
# os.chdir : 디렉터리 위치 변경하기
# os.getcwd : 디렉터리 위치 돌려받기
# os.system : 시스템 명령어 호출하기
# os.popen : 실행한 시스템 명령어의 결괏값 돌려받기
import os
print(os.environ)

# shutil : 파일을 복사해 주는 모듈
# glob : 특정 디렉터리에 있는 파일들을 리스트로 만들어 주는 모듈
# tempfile : 파일을 임시로 만들어서 사용할 때 유용한 모듈

# time : 시간과 관련된 모듈
# time.time : 현재시간을 실수형태로 돌려주는 함수
# time.localtime : time.time()으로 돌려받은 실수 값을 통해 연,월,일,시,분,초의 형태로 바꿔 튜플 형태로 돌려주는 함수
# time.asctime : time.localtime()으로 받은 튜플 값을 활용해 알아보기 쉬운 형태로 돌려주는 함수
# time.ctime : asctime 과 다르게 항상 현재 시간만을 돌려준다.
# time.strftime : 시간에 관계된 것을 세밀하게 표현하는 여러가지 포맷 코드를 제공
#  - %a : 요일 줄임말                         ex) Mon
#  - %A : 요일                                ex) Monday
#  - %b : 달 줄임말                           ex) Jan   
#  - %B : 달                                  ex) January
#  - %c : 날짜와 시간                         ex) 23/04/07 15:45:21
#  - %d : 날(day)                             ex) [04, 29]
#  - %H : 시간(24h)                           ex) [59, 23]
#  - %I : 시간(12h)                           ex) [58 ,12]
#  - %j : 1년 중 누적 날짜                    ex) [001, 366]
#  - %m : 달                                  ex) [01, 12]
#  - %M : 분                                  ex) [01, 59]
#  - %p : AM | PM                             ex) AM
#  - %S : 초                                  ex) [00, 59]
#  - %U : 1년 중 누적 주 (일요일 시작)        ex) [00, 53]
#  - %w : 숫자로 된 요일                      ex) [0(월), 6]
#  - %W : 1년 중 누적 주 (월요일 시작)        ex) [00, 53]
#  - %x : 현재 설정된 지역 기반 날짜          ex) 06/01/01
#  - %X : 현재 설정된 지여 기반 시간          ex) 13:22:21
#  - %Y : 연도                                ex) 2023
#  - %Z : 시간대                              ex) 대한민국 표준시
#  - %% : 문자                                ex) %
#  - %y : 세기 부분 제외 연도                 ex) 01

# time.sleep : 루프 안에서 자주 사용, 일정한 시간 간격을 두고 루프 실행

# Calendar : 파이썬에서 달력을 볼 수 있게 해주는 모듈
import calendar
# calendar.calendar(연도) : 그 해의 전체 달력 보여줌
print(calendar.calendar(2023))
# calendar.prcal(연도) : 위와 동일
# calendar.prmonth(연도, 달) : 해당 연도의 특정 달만 보여줌
print(calendar.prmonth(2023, 4))
# calendar.weekday(연, 월, 일) : 그 날짜에 해당하는 요일을 돌려줌 0~6(월~일)
# calendar.monthrange(연, 월) : 해당 월의 1일이 무슨요일인지와 며칠까지 있는지 튜플형태로 리턴

# random : 난수 발생 모듈

# webbrowser : 기본 웹 브라우저를 자동으로 실행하는 모듈

# threading : 스레드를 다루는 모듈

