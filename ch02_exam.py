# Q1. 홍길동 씨의 과목별 점수는 다음과 같다. 홍길돝ㅇㅊ 씨의 평균 점수를 구해 보자.
#  국어 80, 영어 75, 수학 55
# sol1) 변수에 담에 사칙연산
kor = 80
eng = 75
math = 55

avg = (kor+eng+math)/3
print(avg)

# sol2) 딕셔너리를 활용한 연산
hong = {'kor':80,'eng':75,'math':55}
davg = (hong['eng']+hong['kor']+hong['math']) / len(hong.keys())

print(davg)

# Q2. 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법에 대해 말해보자.
# sol) %를 활용해 나머지 연산 결과가 0이 아니면 홀수
if(13%2==0):
    print("짝수")
else:
    print("홀수")

# Q3. 홍길동씨의 주민등록번호는 881120-1068234이다.
#      홍길동씨의 주민등록번호를 년월일(YYYYMMDD)부분과 그 뒤의 숫자 부분으로 나우어 출력해보자.
# sol) 6번째 인덱스 전후로 슬라이싱해서 출력
pin = '881120-1068234'

yyyymmdd = pin[:6]
print('년월일 : '+yyyymmdd)
num = pin[7:]
print('뒷자리 : '+num)

# Q4. 주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다. 주민등록번호에서 성별을 나타내는
#     숫자를 출력해보자
# sol) 7번쨰 인덱스 출력
print(pin[7])

# Q5. 다음과 같은 문자열 'a:b:c:d' 가 있다. 문자열의 replace 함수를 사용하여 a#b#c#d로 바꿔서 출력해보자.
# sol) 
str = 'a:b:c:d'
print(str.replace(':','#'))

# Q6. [1, 3, 5, 4, 2] 리스트를 [5, 4, 3, 2, 1]로 만들어보자
# sol)
list1 = [1, 3, 5, 4, 2]

list1.sort() # 오름차순 정렬
print(list1)
list1.reverse() # 내림차순 정렬
print(list1)

# Q7. ['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력해 보자.
# sol) 리스트의 join 함수 활용
list2 = ['Life', 'is', 'too', 'short']
result = " ".join(list2)
print(result)

# Q8. (1, 2, 3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 보자.
# sol)
tup = (1,2,3)
tup = tup+(4,)
print(tup)

# Q9. 다음과같은 딕셔러니 a가 있다.
# >>> a = dict()
# >>> a
# {}
# 다음 중 오류가 발생하는 경우를 고르고, 그 이유를 설명해 보자.
# 1. a['name'] = 'python'
# 2. a[('a',)] = 'python'
# 3. a[[1]] = 'python'
# 4. a[250] = 'python'
# sol) 3번, 
#    >> 3번을 제외한 나머지는 변하지 않는 값이고, 3번의 리스트의 1번 인덱스가 변할 수 있음

# Q10. 딕셔너리 dic 에서 'B'에 해당되는 값을 추출해 보자.
# sol) 딕셔너리의 key 값이 'B'인 값을 result 변수에 저장 후 출력
dic = {'A':90, 'B':80, 'C':70}
result = dic['B']
print(dic)
print(result)

# Q11. a 리스트에서 중복 숫자를 제거해 보자.
# sol) set 함수를 이용해 집합 리스트 활용
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)

# Q12. 파이썬은 다음처럼 동일한 값에 여러개의 변수를 선얼할 수 있다.
#      다음과 같이 c, d 변수를 선언한 후 c의 두 번째 요솟값을 변경하려면 d 값은 어떻게 될까?
#      그리고 이런 결과가 나오는 이유에 대해 설명해 보자.
#  c = d = [1, 2, 3]
#  c[1] = 4
#  print(d)
# sol) c, d 변수 모두 같은 주소값을 참조하므로 c[1] 요소를 바꾼 후 d를 출력하더라도 c[1]요소를 바꾼 것과 같은 [1, 4, 3]이 출력된다.
c = d = [1, 2, 3]
c[1] = 4
print(d)
# so12) 주소 값을 다르게 참조하기 위해서는 copy 함수 혹은 리스트를 복사하여 만들어준다.
e = [1, 2, 3]
f = e[:]
e[1] = 4
print(e)
print(f)
