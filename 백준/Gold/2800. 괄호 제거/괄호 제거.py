code = input().rstrip()

stack = []
matchPair = []

for i in range(len(code)):
    if code[i] == "(":
        stack.append(i)
    elif code[i] == ")":
        matchPair.append((stack.pop(),i))

#matchPair.sort() #front가 작은놈이 사전상 무조건 제일 작음
boolean = [True] * len(code)
ans = set()

flg = False
def removeBracket(index : int):
    global flg

    if index == len(matchPair):
        if not flg: flg = True
        else:
            ans.add("".join([code[i] for i in range(len(code)) if boolean[i]]))
        return

    removeBracket(index + 1)

    boolean[matchPair[index][0]] = boolean[matchPair[index][1]] = False
    removeBracket(index + 1)
    boolean[matchPair[index][0]] = boolean[matchPair[index][1]] = True

removeBracket(0)
for case in sorted(ans):
    print(case)



