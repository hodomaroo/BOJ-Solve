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

string = input()
fail = ConstFail(string)

if not KMP(inputStr=input() * 2, target= string, fail=fail):
    print(0)
    exit(0)
    
    
#v가 Fail이 될 수 있음을 증명하려면..  fail[-1]이 v로 나누어 떨어짐
for v in range(1,len(string) + 1):
    #1 / 2 / 3다 패턴이 될 수 있음...
    if v != len(string) and (len(string) % v or fail[-1] % v or (len(string) // v != (fail[-1] // v + 1))): continue
    print(len(string) // v) #패턴의 개수!
    exit(0)
#b를 