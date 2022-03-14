import sys
line = int(input())
sys.setrecursionlimit(10**5)

def func(row : int) -> None:
    if row == line: return
    func_line(0,line - row-1)
    print()

    func(row+1)

def func_line(index,start):
    if index == line: return

    if index < start: print(" ", sep="", end="")
    else: print("*",sep="",end="")

    func_line(index+1,start)

func(0)


