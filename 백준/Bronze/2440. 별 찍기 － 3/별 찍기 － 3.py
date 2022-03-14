import sys
sys.setrecursionlimit(10**5)

def printLine(count : int):
    if not count: return
    print("*", sep="", end="")
    printLine(count-1)

def handleLines(remain : int) -> None:
    if not remain: return
    printLine(remain)
    print()

    handleLines(remain-1)
handleLines(int(input()))








