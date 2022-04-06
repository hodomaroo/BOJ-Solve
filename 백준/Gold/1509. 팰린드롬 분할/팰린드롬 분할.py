string = list(input().rstrip())
isPel = [[False] * len(string) for _ in range(len(string))]    #isPel[i][j]리턴

for i in range(len(string)):
    isPel[i][i] = True
    if i != len(string) -1:
        isPel[i + 1][i] = isPel[i][i + 1] = (string[i] == string[i + 1])  # 둘의 팰린드롬 여부 반환
#길이 2까지의 팰린드롬 여부 반환 완료

for diff in range(2,len(string)):  #간격 한칸부터 시작
    for i in range(len(string) - diff):
        isPel[i + diff][i] = isPel[i][i + diff] = isPel[i + 1][i + diff - 1] and string[i] == string[i + diff]

sliceDp = [i+1 for i in range(len(string) + 1)]
sliceDp[-1] = 0
#문자 길이가 i 일 때, 필요한 분할의 최소 개수

for i in range(1,len(string)):
    for between in range(i+1):    #between ~ i가 팰린드롬일때 between-1의 최소분할 + 1이 답
        if isPel[between][i]:
            sliceDp[i] = min(sliceDp[i],sliceDp[between-1] + 1)
#print(sliceDp)
print(sliceDp[-2])
