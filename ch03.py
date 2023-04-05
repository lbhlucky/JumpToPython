# 제어문

# if 문 
# 조건을 판단하여 해당 조건에 맞는 상황을 수행하는 데 사용

# 기본 구조
# if 조건문:
#    실행문
# else:
#    실행문

# 비교연산자
# x < y   : x가 y보다 작다
# x > y   : x가 y보다 크다 
# x == y  : x와 y가 같다
# x != y  : x와 y가 같지 않다
# x >= y  : x가 y보다 크거나 같다
# x <= y  : x가 y보다 작거나 같다.

a = 2
if a == 3:
    print('정답')
else:
    print("오답")

# and(&), or(|), not
# x and(&) y : x, y 모두 True 일 때만 True
# x or(|) y : x, y 둘 중 하나라도 True면 True
# not x : x가 Ture 면 False, x가 False 면 True

# x in s, x not in s
# x (not) in 리스트
# x (not) in 튜플
# x (not) in 문자열

# 다양한 조건을 판단하는 elif

# 기본 문법
# if 조건문:
#     조건문이 True일 경우 실행 할 실행문
# elif 조건문2:
#     조건문2가 True일 경우 실행 할 실행문
# elif 조건문n:
#     조건문n이 True일 경우 실행 할 실행문
# else:
#     위 조건이 False일 경우 실행 할 실행문

# 조건부 표현식
# 조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우
# ex)
score = 99 
msg = "pass" if score >= 80 else "fail"
print(msg)

# While 문 - 조건이 True 인 동안 반복 실행
# 기본 구조
# while 조건문:
#     실행문

# ex) 나무 10번 찍기
a = 0
while a < 10:
    a += 1
    print("나무 %d번 찍음" % a)

# 반복문 강제로 빠져나가기 (break)
coke = 10
coin = 500

while coin:
    print("콜라 1개 줌")
    coke -= 1
    if coke == 0:
        print("콜라 없음")
        break

# 반복문 처음으로 돌아가기 (continue)

# ex2) 1부터 10까지의 숫자 중 3의 배수를 뺀 나머지 값을 출력해 보자
# sol1)
a = 1
while a < 11:
    if a % 3 != 0:
        print(a, end=" ")
    a += 1
print("\n")
# sol2) continue 활용
a = 0
while a < 10:
    a += 1
    if a % 3 == 0:
        continue
    print(a, end=" ")
print("\n")
# 무한 루프 - 무한히 반복하는 문장
# while True:
#     print("ctrl + c를 눌러 빠져나가기")

# for문

# 기본 구조
# for 변수 in 리스트(튜플, 문자열):
#   실행문

test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

# for문과 함께 자주 사용되는 range 함수
# range(시작숫자, 끝숫자+1)
# ex) 1 ~10 까지라면 range(1, 11)

# range 함수와 for문을 활용해 구구단

for dan in range(2, 10):
    print("< %d 단 >" % dan)
    for num in range(1,10):
        print("%d * %d = %d" % (dan, num, (dan*num)))

