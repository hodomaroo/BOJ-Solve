from collections import deque

#프로그램 코드의 길이는 최대 1000 
#KMP의 각 글자를 단어로 사용!
#가장 짧은 문자열을 고르는게 로직상 가장 효율적임
#K개 이상의 연속된 코드를 골라서, 
# KMP Fail Func을 2개씩(양방향)으로 만들고, 쿼리 수행

#속임수였네...? -> 길이 K짜리만 있으면 됨 ㅋㅋㅋㅋㅋㅋㅋㅋ 어차피 K이상이면 당연히 K도 되겠지
#경우의 수 -> (Mi - K) * SUM(M) -> 996 *10^5 -> 10^8.. zㅋㅋㅋㅋ 간당간당

from typing import NoReturn


def ConstFail(target : list) -> list:
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

def KMP(inputStr : list , target : list, fail : list) -> list:
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


n,k = map(int,input().split())
words = []

for _ in range(n):
    input()
    words.append(list(map(int,input().split())))
    
pattern = deque(words[0][:k - 1])
rv = deque(words[0][:k-1][::-1])


for i in range(k - 1, len(words[0])):
    pattern.append(words[0][i])
    rv.appendleft(words[0][i])
    
    flg = True
    fail1 = ConstFail(pattern)
    fail2 = ConstFail(rv)
    
    for v in words:
        if not KMP(fail=fail1,target=pattern,inputStr=v) and not KMP(fail=fail2,target=rv,inputStr=v):
            flg =  False
            break
    
    if flg:
        print("YES")
        exit(0)
        
    pattern.popleft()
    rv.pop()
print("NO")
                
