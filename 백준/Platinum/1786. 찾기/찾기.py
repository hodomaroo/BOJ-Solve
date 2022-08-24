import sys
input = sys.stdin.readline

def ConstFail(target : str) -> list:
    # fail(x) -> y
    fail = [0] * (len(target) + 1)

    #0에서는 무조건 Root로 회귀함
    #1 -> 0번 문자와 같은 경우 이동 가능한 상태
    for i in range(2, len(target) + 1):
        fail[i] = fail[i - 1]

        while fail[i] != 0 and target[fail[i]] != target[i - 1]:
            fail[i] = fail[fail[i]]

        fail[i] += (target[fail[i]] == target[i - 1])

    return fail

def KMP(inputStr : str , target : str, fail : list) -> list:
    matchList = []
    targetLength = len(target)

    status = 0
    for i in range(len(inputStr)):
        while status != 0 and (status == targetLength or inputStr[i] != target[status]):
            status = fail[status]

        status += target[status] == inputStr[i]

        if status == targetLength:
            matchList.append(i - targetLength + 2)
    return matchList

inputString = input().rstrip()
targetString = input().rstrip()

res = KMP(inputString, targetString, ConstFail(targetString))
print(len(res))
print(*res)

