while True:
    histogram = [0] + list(map(int,input().split()))[1:] + [0]
    if len(histogram) == 2 and histogram[1] == 0: exit()

    stack = []
    ans = 0
    for i,v in enumerate(histogram):
        while stack and stack[-1][1] > v:
            index, height = stack.pop()
            ans = max(ans, height * (i - stack[-1][0] - 1))

        stack.append((i,v))
    print(ans)





