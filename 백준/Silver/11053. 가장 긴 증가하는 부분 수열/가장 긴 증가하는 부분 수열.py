import sys
import bisect
input = sys.stdin.readline
N = int(input())
word=  list(map(int,input().split()))
""" O(N^2)


dp = [1 for _ in range(N)]

for i in range(1,N):
    for ci in range(0,i):
        if word[ci] < word[i] and dp[ci] >= dp[i]:
            dp[i] = dp[ci] + 1
print(max(dp))
"""

""" O(NlogN)"""
ans = [word[0]]

for idx in range(1,len(word)):
    if word[idx] > word[idx-1]:
        find = bisect.bisect_left(ans,word[idx])

        if find >= len(ans):
            ans.append(word[idx])   #길이가 추가되는건 제일 값이 클때만
        else:
            ans[find] = word[idx]

    elif word[idx] < word[idx-1]:
        find = bisect.bisect_left(ans, word[idx])
        ans[find] = word[idx]
print(len(ans))