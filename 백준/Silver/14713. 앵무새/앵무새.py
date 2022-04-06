from collections import deque
n = int(input())
wordDict = dict()
wordQueue = [deque(list(input().split())) for i in range(n)]

for word in list(input().rstrip().split()):
    index = None

    for i in range(n):
        if not wordQueue[i]: continue

        if wordQueue[i][0] == word:
            index = wordQueue[i].popleft()
            break
    #유효한 경우에만 찾을것

    if index == None:
        print("Impossible")
        exit()
for i in range(n):
    if wordQueue[i]:
        print("Impossible")
        exit()

print("Possible")

