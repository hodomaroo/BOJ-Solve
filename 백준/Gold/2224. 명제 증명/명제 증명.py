from collections import defaultdict
n = int(input())
matrix = [[False] * 52 for _ in range(52)]


for i in range(n):
    a,b,c = input().split()
    a : str
    c : str

    matrix[ord(a) - ord("A") if a.isupper() else ord(a) - ord('a') + 26][ord(c) - ord("A") if c.isupper() else ord(c) - ord('a') + 26] = True

for i in range(52):
    for j in range(52):
        for k in range(52):
            matrix[j][k] = max(matrix[j][k], matrix[j][i] and matrix[i][k])

ans = []
for i in range(52):
    for j in range(52):
        if i == j or not matrix[i][j]: continue
        str1 = ord("A") + i if i // 26 == 0 else ord("a") + i % 26
        str2 = ord("A") + j if j // 26 == 0 else ord("a") + j % 26
        ans.append((str1,str2))
print(len(ans))
for a,b in ans:
    print(chr(a),"=>",chr(b))