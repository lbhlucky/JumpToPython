# 파이썬 자료형
# 1. 숫자형

# 정수형(int) - 양의 정수, 0, 음의 정수
# 실수형(float) - 소수점이 포함된 숫자
# 8진수(0o, 0O)와 16진수(0x) - 8진수와 16진수

#  사칙연산
a = 3
b = 5

# 더하기
print("a+b=%d" % (a+b))

# 빼기
print("a-b=%d" % (a-b))

# 곱하기
print("a*b=%d" % (a*b))

# 나누기
print("a/b=%d" % (a/b))

# 제곱
print("a**b=%d" % (a**b))

# 나눈 후 나머지 반환
print("a%%b=%d"%  (a%b))

# 나눈 후 몫 반환
print("a//b=%d" % (a//b))

# 2. 문자열 자료형
# - 큰 따옴표(" ")
# - 작은 따옴표(' ')
# - 큰 따옴표 3개 (""" """)
# - 작은 따옴표 3개 (''' ''')

# 문자열 안에 작은 따옴표나 큰 따옴표를 포함시키고 싶을 때
# 다른 따옴표로 감싸기
# ex) '"' , "'"
# 역슬래시 사용
# ex) \' , \"

# 이스케이프코드 
# >> 프로그래밍할 때 사용할 수 있도록 미리 정의해 둔 '문자 조합'
# \n 문자열 안에서 줄 바꿈
# \t 문자열 사이에 탭 간격 줄 때
# \\ 문자\표현
# \' 작은 따옴표 표현
# \" 큰 따옴표 표현
 
# 문자열 연산
head = "Python"
tail = ' is fun!'

# 문자열 더하기
print("head+tail=%s" %(head+tail))

# 문자열 곱하기
print("head*2=%s" %(head*2))

# 문자열 곱하기 응용
print("="*50)
print("문자열 곱하기 응용")
print("="*50)

# 문자열 길이 구하기
print("문자열 길이 구하기 : ",len(head))

# 문자열 인덱싱
# >> 각 문자열의 각 위치에 접근
print("head의 2번째 요소 : ", head[1])
print("head의 마지막 요소 : ", head[-1])

# 문자열 슬라이싱
# >> 문자열에서 특정 단어 추출
print('is fun!에서 is만 추출 : ', tail[1:3])
print('is fun!에서 fun!만 추출 : ', tail[4:])

# 문자열 포매팅
# >> 문자열안에 특정한 값을 바꿔야하는 경우에 사용

# 문자열 포맷 코드
# %s : 문자열(string)
# %c : 문자 1개 (character)
# %d : 정수(integer)
# %f : 실수(flaot)
# %o : 8진수
# %x : 16진수
# # %% : 문자 '%' 사용

#### 문자열 관련 함수 ####

# 문자 개수 세기 (count)
str = "hobby"
print("b의 개수 : ",str.count('b'))

# 위치 알려주기1 (find)
str = 'Life is too short'
print("find활용 : f의 위치 : ",str.find('f'))

# 위치 알려주기2 (index)
str = 'Life is too short'
print("index활용 : f의 위치 : ",str.index('f'))

# 문자열 삽입 (join)
print(",".join('abcd'))

# 소문자를 대문자로 바꾸기 (upper)
print('소문자를 대문자로 바꾸기  >> %s' %'hi'.upper())

# 대문자를 소문자로 바꾸기 (lower)
print('대문자를 소문자로 바꾸기 HI >> %s' %'HI'.lower())

# 왼쪽 공백 지우기 (lstrip)
str = ' hello '
print("왼쪽 공백 지우기 : ",str.lstrip())

# 오른쪽 공백 지우기 (rstrip)
str = ' hello '
print("오른쪽 공백 지우기 : ",str.rstrip())

# 양쪽 공백 지우기 (strip)
str = ' hello '
print("양쪽 공백 지우기 : ",str.strip())

# 문자열 바꾸기 (replace)
str = 'Life is too short'
print("변경 전 : %s" %str)
print("변경 후 : %s" %str.replace('Life', 'Your leg'))

# 문자열 나누기 (split)
str = 'Life is too short'
print("변경 전 : %s" %str)
print("변경 후 : %s" %str.split())

# 리스트
# 하나의 변수에 많은 데이터를 저장하기 위해 사용
# 리스트명 = [요소1, 요소2, 요소3, ''']
# ex) li = [1, 3, 5, 7, 9]

# 리스트 연산
# 1) 더하기 : 두 리스트의 요소가 합쳐진다.
# 2) 곱하기 : 리스트가 반복된다.

# 리스트 관련함수
# 추가(append)
li = [1, 2, 3]
li.append(4)    #li 리스트에 4라는 요소 추가
print(li)

# 정렬(sort) - 오름차순 정렬
# 뒤집기(reverse) - 내림차순 정렬
li.sort()      # 오름차순
print(li)
li.reverse()    # 내림차순
print(li)

# 위치 반환(index) - n번째 요소를 리턴
print(li.index(3))

# 요소 삽입(insert) - 특정 위치에 삽입
#  insert(a, b) - a 위치에 b 삽입
li.insert(0,6)
print(li)

# 요소 제거(remove) - 특정 요소 삭제
# remove(6) - 리스트의 첫번째로 나오는 6 제거
li.remove(6)
print(li)

# 요소 끄집어내기(pop) - 리스트의 마지막 요소 리턴 후 삭제
print(li.pop())

# 리스트의 특정 요소 개수 세기 (count) - 특정 문자가 포함된 개수 리턴
print(li.count(4))

# 리스트 확장(extend) - a리스트에 b리스트 추가
li.extend([6,9])
print(li)

