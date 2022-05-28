import sys

#input = sys.stdin.read
inform = input().rstrip()

count = 0
ans = 0
for idx,s in enumerate(inform):
     count += [-1,1][s == "("]
     if s == ")":
        if inform[idx - 1] == "(":
            ans += count

        else:
            ans += 1 #끄트머
print(ans)


