a,b = map(int,input().split())
values = sorted(zip([0] + list(map(int,input().split())), list(range(a + 1))), key= lambda x : x[0], reverse= True)
pair = [0] * (a + 1)

for v,idx in values[:b]:
    pair[idx] = idx
    
print(*[v for _,v in sorted(values[:min(b,a)], key=lambda x : x[1])[:b]], sep="\n")
print(*[0] * max(0, b - a), sep = "\n")
print(*pair[1:], sep="\n")