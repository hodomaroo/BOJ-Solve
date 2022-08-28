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
fail = ConstFail(list(map(int,input().rstrip().split()))[::-1])

#print(fail)
ans = max(fail)
if ans:
    print(ans,fail.count(ans))
else:
    print(-1)