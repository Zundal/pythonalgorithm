# 재귀호출

# 1부터 n까지의 곱, 팩토리얼(factiorial) 알고리즘

# 재귀적 정의 
#   n! = n * (n - 1)!

# if num == 5
# 1 * 1 = 1
# 1 * 2 = 2
# 2 * 3 = 6
# 6 * 4 = 24
# 24 * 5 = 120
def factiorial(num):
    result = 1
    for i in range(1, num + 1):
        result = result * i
    return result

# 재귀적 factorial
def factiorialRecul(num):
    if num <= 1:
        return 1
    return num * factiorialRecul(num -1)

# 간단한 재귀 함수 호출
def hello():
    print("hello")
    hello()

# 1부터 n까지의 합 recursive
def recursiveSum(num):
    if num <= 0:
        return 0
    return num + recursiveSum(num -1)

# 재귀를 통한 최댓 값 찾기
def recursiveFindMaxNum(numArr, numArrLen):
    if numArrLen == 1: # 종료 조건
        return numArr[0]
    
    maxNum = recursiveFindMaxNum(numArr, numArrLen-1) # 루프처럼 돈다

    if maxNum > numArr[numArrLen - 1]:
        return maxNum
    else:
        return numArr[numArrLen - 1]

arrNum = [123, 5345, 12, 35, 34, 6, 24, 4564, 12]

print(factiorial(5))
print()
# RecursionError: maximum recursion depth exceeded while calling a Python object
# hello() 무한 재귀호출로 인한 에러 발생
print(factiorialRecul(5))
print()
print(recursiveSum(5))
print(recursiveFindMaxNum(arrNum, len(arrNum)))

