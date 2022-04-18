n,m = map(int,input().split())
numbers = sorted(list(map(int,input().split())))
array = []
selNumbers = set()


def func():
    if len(array) == m:
        print(*array)
        return

    for i in numbers:
        if i in selNumbers: continue
        selNumbers.add(i)
        array.append(i)
        func()
        selNumbers.discard(i)
        array.pop()
func()
