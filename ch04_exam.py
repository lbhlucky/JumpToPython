# Q1. 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해보자.
# sol)
def is_odd(num):
    if num % 2 == 0:
        return True
    else:
        return False
print(is_odd(3))    # 3은 홀수이므로 False
print(is_odd(8))    # 8은 짝수이므로 True

# Q2. 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해보자.
#     단, 입력으로 들어오는 수는 정해져 있지 않다.
# sol)
def avg_input_number(*args):
    result = 0
    for i in args:
        result += i
    return result

print(avg_input_number(1,3))    # 1+3의 결과값 4 출력
print(avg_input_number(1,3,6))  # 1+3+6의 결과값 10 출력

# Q3. 다음은 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램이다.
#     input1 = input("첫번쨰 숫자를 입력하세요 : ")
#     input2 = input("두번쨰 숫자를 입력하세요 : ")
#     total = input1 + input2
#     print("두 수의 합은 %s 입니다." %total)
#     만약, 3과 6을 입력했을 때 9가 아닌 36이 출력된다면 수정해보자
# sol)
input_num1 = int(input("첫번째 숫자를 입력하세요 : "))
input_num2 = int(input("두번째 숫자를 입력하세요 : "))
sum = input_num1 + input_num2
print("두 수의 합은 %d 입니다." %sum)

# Q4. 다음 중 출력 결과가 다른 것 하나를 골라 보자.
# 1. print("you" "need" "python")
# 2. print("you" + "need" + "python")
# 3. print("you", "need", "python")
# 4. print("".join(["you", "need", "python"]))
# sol) 3번
# ,는 띄어쓰기 역할을 함

# Q5. 다음은 "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.
# f1 = open("test.txt", 'w')
# f1.write("Life is too short")
# 
# f2 = open("test.txt", 'r')
# print(f2.read())
# 이 프로그램은 우리가 예상한 "Life is too short"라는 문장을 출력하지 않는다.
# 우리가 예상한 값을 출력할 수 있도록 프로그램을 수정해보자.
# sol1)
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()

# sol2)
with open("test1.txt", 'w', encoding="UTF-8") as f1:
    f1.write("Your leg is too short")
with open("test1.txt", 'r', encoding="UTF-8") as f2:
    print(f2.read())

# Q6. 사용자의 입력을 파일(test3.txt)에 저장하는 프로그램을 작성해보자.
#     단, 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.
# sol)
user_input = input("저장할 내용을 입력하세요 : ")
with open("test3.txt", 'a', encoding="UTF-8") as f:
    f.write(user_input)
with open("test3.txt", 'r', encoding="UTF-8") as tf:
    print(tf.read())

# Q7. 다음과 같은 내용을 지닌 test.txt 가 있다.
#     이 파일의 내용 중 'java'라는 문자열을 'python'으로 바꾸어 저장해 보자
# Life is too short
# you need java
tf = open("test2.txt", 'w', encoding="UTF-8")
body = tf.write("Life is too short \n you need java")
tf.close()

tf1 = open("test2.txt", 'r', encoding="UTF-8")
body = tf1.read()
tf1.close()

body = body.replace("java", "python")

tf2 = open("test2.txt", 'w', encoding="UTF-8")
tf2.write(body)
tf2.close()

tf3 = open("test2.txt", 'r', encoding="UTF-8")
print(tf3.read())
tf3.close()
