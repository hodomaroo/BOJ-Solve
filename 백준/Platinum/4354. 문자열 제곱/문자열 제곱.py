from re import T


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
    
while True:
    s = input()
    if s == ".":   
        break
    fail = ConstFail(s)
    availableList = []
    for i in range(1, len(fail)):
        if fail[i] and fail[i] < fail[i-1]:
            availableList = []
        availableList.append(i)
    availableList.append(i)
    
    flg = False
    for v in availableList:
        if len(s) % v == 0 and fail[-1] % v == 0 and len(s) // v == fail[-1] // v + 1:
            print(len(s) // v)
            flg = True
            break
    if not flg:
        print(1)
        
        