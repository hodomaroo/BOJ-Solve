meetings = sorted([list(map(int,input().split())) for _ in range(int(input()))],key=lambda x : (x[1],x[0]))
time,count = 0,0
for start,end in meetings:
    if start < time: continue
    time = end
    count += 1
print(count)