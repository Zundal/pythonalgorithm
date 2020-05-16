# 최대값 찾기

# 먼저 리스트 사용법
# a = [5, 7, 9]
# print(a);
# print(a[0])
# print(a[2])
# print(len(a))

# 배열의 가장 큰 수를 찾아주는 함수
def findMaxNum(arr):
    resultMaxNum = 0;
    for i in range(len(arr)):
        if resultMaxNum < arrNum[i]:
            resultMaxNum = arrNum[i]
    return resultMaxNum;

# 리스트 숫자가 n개 있을 때 가장 큰 값이 있는 위치 번호를 돌려주는 알고리즘
def findMaxIndex(arr):
    resultIndexNum = 0;
    for i in range(len(arr)):
        if arrNum[resultIndexNum] < arrNum[i]:
            resultIndexNum = i
    return resultIndexNum;

arrNum = [123, 535, 23, 94, 2034, 994, 44, 987];

print(findMaxNum(arrNum));
print(findMaxIndex(arrNum));
