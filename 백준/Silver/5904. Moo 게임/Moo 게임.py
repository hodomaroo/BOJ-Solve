n = int(input())
length = 3
cha = 0

while length <= n:
    length = length * 2 + cha + 4
    cha += 1
#m o o m o o o m o o m o o o o m o o m o o o m o o
#1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
flg = False
def judge(index : int, length : int, c : int):
    if not c:
        return index == n

    nextLength = (length - 3 - c) // 2
    if index + nextLength == n: return True

    if judge(index, nextLength, c - 1): return True
    if judge(index + length - nextLength , nextLength, c - 1): return True

    return False
print(["o","m"][judge(1,length,cha)])




