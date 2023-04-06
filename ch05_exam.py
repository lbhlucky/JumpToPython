# Q1.다음은 Calculator 클래스 이다.
# class Calculator:
#     def __init__(self):
#         self.value = 0
#     def add(self, val):
#         self.value += val
# 위 클래스를 상속하는 UpgradeCalculator를 만들고 값을 뺄 수 있는 minus 메서드를 추가해 보자.
# 즉, 다음과 같이 동작하는 클래스를 만들어야한다.
# cal = UPgradeCalculator()
# cal.add(10)
# cal.minus(7)
# print(ca.value)

class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)

# Q2. 객체변수 value가 100 이상의 값은 가질 수 없도록 제한하는 MaxLimitCalculator 클래스를 만들어보자/
#     즉, 다음과 같이 동작해야 한다.
# cal = MaxLimitCalculator()
# cal.add(50)
# cal.add(60)

# print(cal.value)
# 단, 반드시 다음과 같은 Calculator1 클래스를 상속해서 만들어야한다.
# class Calculator1:
#     def __init__(self):
#         self.value = 0
#     def add(self, val):
#         self.value += val

class Calculator1:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator1):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)

# Q3. 다음 결과를 예측해 보자.
# Q3-1. all([1, 2, abs(-3)-3])
# >> all 함수는 모든 것이 참일 경우에만 True 이다.
#    abs(-3)-3은 0 이므로 False False 출력
# Q3-2 chr(ord('a')) == 'a'
# >> chr 함수는 아스키 코드를 입력 받아 문자로 변환 해주는 것
#    ord 함수는 문자를 입력 받아 문자로 변환 해주는 것
#    'a'를 아스키 코드로 입력 받은 후 chr 함수를 통해 다시 문자로 반환 받았으므로 같다. True 출력

# Q4. filter 와 lambda를 사용하여 리스트[1, -2, 3, -5, 8, -3]에서 음수를 제거해보자.
# sol)
print(list(filter(lambda x:x>0, [1, -2, 3, -5, 8, -3])))

# Q5.234라는 10진수의 16진수는 다음과같이 구할 수 있다.
#    hex(234)   : 0xea
#    이번에는 반대로 16진수 문자열 0xea를 10진수로 변경해 보자.
# print(int(0xea))
print(int('0xea', 16))

# Q6. map 과 lambda를 사용하여 [1, 2, 3, 4] 리스트의 각 요솟값에 3이 곱해진 리스트 [3, 6, 9, 12]를 만들어보자.\
print(list(map(lambda x:x*3, [1,2,3,4])))

# Q7. 다음 리스트의 최댓값과 최솟값의 합을 구해보자.
# [-8, 2, 7, 5, -3, 5, 0, 1]
li = [-8, 2, 7, 5, -3, 5, 0, 1]
print(max(li)+min(li))  # max = 7 , min = -8

# Q8. 17 / 3의 결과를 반올림 해라.
print(round(17/3, 4))

# Q9. 다음과 같이 실행할 때 입력값을 모두 더하여 출력하는 스크립트를 작성해보자.
#     sys 모듈의 argv 사용
import sys

nums = sys.argv[1:]

result = 0
for num in nums:
    result += int(num)
print(result)

# Q10. os 모듈을 사용하여 다음과 같이 동작하도록 코드를 작성해 보자.
#      os 모듈의 chdir 사용
import os
os.chdir("c:/Users/lbhlu/OneDrive/바탕 화면/Python/JumpToPython/")

result1 = os.popen("dir")

print(result1.read())

# Q11. 생략

# Q12. time 모듈을 사용하여 현재 날짜와 시간을 다음과 같은 형식으로 출력해보자.
#      time 모듈의 strftime을 사용
import time

print(time.strftime("%Y/%m/%d %H:%M:%S"))

# Q13. 생략