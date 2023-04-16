# 구구단 프로그램(함수) 만들기
# n 입력 시 n 단 출력
def GuGuDan(n):
    result = []
    i = 1
    while i < 10:
        result.append(n*i)
        i += 1
    return result

print(GuGuDan(6))    

# 3과 5의 배수 합 구하기
# n = 1
# while n < 1000:
#     print(n)
#     n += 1

result1 = 0
for n in range(1,1000):
    if n % 3 == 0 or n % 5 == 0:
        result1 += n
print(result1)

# 게시판 페이징 하기
def getTotalPage(m, n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1

print(getTotalPage(5, 10)) 
print(getTotalPage(15, 10)) 
print(getTotalPage(25, 10)) 
print(getTotalPage(30, 10)) 
