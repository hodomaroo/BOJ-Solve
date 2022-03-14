import sys
sys.setrecursionlimit(10**5)

def printChar(count : int, symbol : str) -> None:
    if not count: return
    print(symbol, end="")
    printChar(count-1,symbol)

def handleLines(row : int, limit : int) -> None:
    if row == limit: return
    printChar(abs((limit-1) // 2 - row)," ")
    printChar(abs((limit - 1) // 2 - abs((limit - 1) // 2 - row)) * 2  + 1, "*")
    print()

    handleLines(row + 1,limit)

handleLines(0,int(input()) * 2 - 1)
