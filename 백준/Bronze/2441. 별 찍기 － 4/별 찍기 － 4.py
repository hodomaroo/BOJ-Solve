import sys
sys.setrecursionlimit(10**5)

def printLine(index : int, convert : int, limit : int) -> None:
    if index == limit: return
    print(" " if index < convert else "*", end="")
    printLine(index + 1,convert,limit)

def handleLines(row : int, limit : int) -> None:
    if row == limit: return
    printLine(0,row,limit)
    print()

    handleLines(row + 1,limit)

handleLines(0,int(input()))
