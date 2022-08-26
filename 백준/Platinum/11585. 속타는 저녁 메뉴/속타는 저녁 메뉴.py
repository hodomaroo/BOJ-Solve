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
    
n = int(input().rstrip())
fail = ConstFail(list(input().rstrip().split()))
input().rstrip()

"""
availableList = []
for i in range(1, len(fail)):
    if fail[i] and fail[i] < fail[i-1]:
        availableList = []
    availableList.append(i)
availableList.append(i)
"""

for v in range(1, n + 1):
    if v != n and (n % v or fail[-1] % v or (n // v != (fail[-1] // v + 1))): continue
    
    print(1,"/",v, sep = "")
    exit(0)