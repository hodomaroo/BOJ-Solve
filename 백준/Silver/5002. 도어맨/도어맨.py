n = int(input())
pat = [-1 if v == "W" else 1 for v in list(input())]
tot = 0

for i in range(len(pat)):
    if pat[i] != pat[min(i+1, len(pat) - 1)]:
        pat[i + 1] = [-1, 1][tot > 0]
        tot += [1, -1][tot > 0]
    
    else:
        tot += pat[i]
        
    if abs(tot) > n:
        print(i)
        exit(0)
        
print(i + 1)

    
    