# 1 부터 n 까지의 합 구하기
# 안정식 작성
def sum_n(n):
    resultSum = 0; # 더한 결과 값
    for i in range(n):
        
        resultSum += i+1;
    return resultSum;    

# 가우스 방식
# 1부터 n까지 연속한 숫자의 합을 구하는 알고리즘
# 입력n
# 출력 1부터 n까지의 숫자를 더한 값
def sum_g(n):
    return n * (n+1) // 2 # 슬래시 두개는 정수 나누셈을 의미한다

# 입력 값까지 제공의 알고리즘
def comp_s(n):
    resultComp = 0;
    for i in range(n):
        resultComp = i*i;
    return resultComp;

print(sum_n(10));
print(sum_n(100));
print()
print(sum_g(10));
print(sum_g(100));
print()
print(comp_s(10));