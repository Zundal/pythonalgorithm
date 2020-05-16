# 동명이인 찾기

# set은 여러 개의 정보를 넣을 수 있지만 집합 하나에는 같은 자료가 중복되어 들어가지 않는다
# s = set()
# s.add(1)
# s.add(2)

# print(s)

# print(s == {2,1}) # 집합은 순서를 상관하지 않는다.

# 두번 이상 나온 이름 찾기
def repeatName(name):
    setRepeatName = set()
    for i in range(0, len(name)):
        cnt = 0
        for j in range(0, len(name)):
            if(nameArr[i] == nameArr[j]):
                cnt += 1
                if(cnt >= 2):
                    setRepeatName.add(nameArr[i])
    
    return setRepeatName

# 입력한 이름 배열 두명씩 짝을 지어주는 프로그램
def makePair(nameArr):
    resultPair = []

    for i in range(0, len(nameArr)):
        for j in range(0, len(nameArr)):
            if(nameArr[i] != nameArr[j]):
                resultPair.append(nameArr[i]+"-"+nameArr[j])
    return resultPair


nameArr = ["안정식", "한진선", "0118", "박선영", "안정식", "박선영"] # 두번 이상 나온 이름 찾기
namePair = ["안정식", "한진선", "0118", "박선영"] # 페어 이름 배열

print(repeatName(nameArr))
print()
print(makePair(namePair))



