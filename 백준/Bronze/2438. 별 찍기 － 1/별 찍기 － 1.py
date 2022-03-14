import sys
sys.setrecursionlimit(5050)

line = int(input())

def func(row,col):
    if row >= line: return
    print("*\n" if row == col else "*",sep="",end="")
    func(row + (col == row),(col + 1) * (col != row))
func(0,0)
