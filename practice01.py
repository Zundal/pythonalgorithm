import math # 수학모듈 사용

# 절대 값 알고리즘 1 부호 (판단)

# 입력 실수 a
# 출력 a의 절대값

def abs_sgin(a):
    if a >= 0:
        return a
    else:
        return -a

# 절대값 알고리즘 2(제곱-제곱근)
# 입력 실수 a

def abs_square(a):
    b = a * a
    return math.sqrt(b) # 수학 모듈의 제곱근

print(abs_square(5))
print(abs_square(-3))
print()
print(abs_square(5))
print(abs_square(-3))

