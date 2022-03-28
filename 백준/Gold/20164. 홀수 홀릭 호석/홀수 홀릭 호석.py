def getNumberOfOdd(number : str) -> int:
    return sum(int(v)%2 for v in number)

def OddHolic(number : str) -> int:
    if len(number) == 1: return (int(number) % 2, int(number) % 2)
    base = getNumberOfOdd(number)  #현재 숫자의 홀수 갯수 구하기

    maxOdd = - float("inf")
    minOdd = float("inf")

    if len(number) == 2:
        minResult,maxResult = OddHolic(str(int(number[0]) + int(number[1])))
        maxOdd = max(maxOdd, maxResult)
        minOdd = min(minOdd, minResult)
    else:
        for i in range(1,len(number)-1):    #최소 마지막에서 두칸까지는 남겨야함
            for j in range(i+1,len(number)): #최소 한칸은 남겨야함
                minResult,maxResult = OddHolic(str(int(number[:i]) + int(number[i:j]) + int(number[j:])))
                maxOdd = max(maxOdd,maxResult)
                minOdd = min(minOdd,minResult)

    return (base + minOdd,base + maxOdd)

print(*OddHolic(input().rstrip()))
