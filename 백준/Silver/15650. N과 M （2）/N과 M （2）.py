n,m = map(int,input().split())

res = []
def func(startIndex : int):
    if len(res) == m:
        print(*res)

    for i in range(startIndex, n + 1):
        res.append(i)
        func(i + 1)
        res.pop()
func(1)