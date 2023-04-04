# Q1. 다음 코드의 결괏값은 무엇일까?
str = "Life is too short, you need python"

if "wife" in str: print("wife") # wife 는 없으므로 거짓
elif "python" in str and "you" not in str: print("python")  # python, you 모두 있으므로 거짓
elif "shirt" not in str: print("shirt") # shirt 는 없으므로 참
elif "need" in str: print("need")   # need 는 있으므로 참
else: print("none") # 다 거짓이라면 "none" 출력
# 세번째 조건문이 제일 먼저 참이므로 shirt 출력

# Q2. while 문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
result = 0
num = 1
while num <= 1000:
    if num%3==0:
         result += num
    num += 1

print(result)

# Q3. while 문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해보자
star = 0
while True:
     star += 1
     if star > 5: break
     print("*"*star)

# Q4. for 문을 사용해 1부터 100까지의 숫자를 출력해보자
for i in range(1,101):
     print(i)

# Q5. A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
#     [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
#     for문을 사용하여 A 학급의 평균 점수를 구해 보자.

score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
avg = 0
for scr in score:
     total += scr
avg = total / len(score)
print(avg)
          
# Q6 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.
# numbers = [1, 2, 3, 4, 5]
# result = []
# for n in numbers:
#      if n % 2 == 1:
#           result.appen.(n*2)
# 위 코드를 리스트 내포를 사용해 표현해 보자.

numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n % 2 == 1]
print(result)


