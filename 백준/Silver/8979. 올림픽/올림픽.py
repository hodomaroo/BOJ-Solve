n, k = map(int,input().split())
ranks = [0] * (n + 1)

countries = sorted([list(map(int,input().split())) for _ in range(n)],key=lambda x : (x[1],x[2],x[3]),reverse=True)

beforeGsb = (float("inf"),0,0)
rank = 0
count = 1

for code,g,s,b in countries:
    if (g,s,b) < beforeGsb:
        rank += count
        beforeGsb = (g,s,b)
        ranks[code] = rank
        count = 1
        continue
    ranks[code] = rank
    count += 1
print(ranks[k])