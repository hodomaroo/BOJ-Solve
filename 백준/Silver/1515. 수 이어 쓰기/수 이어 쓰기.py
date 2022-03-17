number = list(map(int,list(input().rstrip())))[::-1]

maxNumber = 0
numList = [1]
index = 0

def countUp(numList : list):
    numList[0] += 1
    index = 0
    while numList[index] == 10:
        numList[index] = 0
        if len(numList) == index + 1:
            numList.append(1)
            break
        else:
            index += 1
            numList[index] += 1

count = 0
while True:
    count += 1

    for n in numList[::-1]: #뒤쪽부터 검사 --> 뒤가 제일 큰자리
        if number and n == number[-1]:
            number.pop()
    if not number: break

    countUp(numList)

print(*numList[::-1],sep="")
