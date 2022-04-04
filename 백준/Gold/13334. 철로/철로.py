import sys

input = sys.stdin.readline

n = int(input())
pos = []

vCount = [0] * n   #n번째 home / off boolean 여부

pos = []
count = 0

for i in range(n):
    home,office = map(int,input().split())
    pos.append((home, i))    #i번째 친구를 넣고 빼고 할것
    pos.append((office, i))

railLen = int(input())

pos.sort()
s_index,e_index = 0,0

ans = 0
while s_index < len(pos):
    #print(s_index,e_index)
    while e_index < len(pos) and pos[e_index][0] <= pos[s_index][0] + railLen:
        position,index = pos[e_index]

        vCount[index] += 1
        count += vCount[index] == 2

        e_index += 1

    ans = max(count,ans)
    next_s_index = s_index

    while next_s_index < len(pos) and pos[next_s_index][0] == pos[s_index][0]:
        position, index = pos[next_s_index]

        if vCount[index] == 2:
            count -= 1

        vCount[index] -= 1
        next_s_index += 1

    s_index = next_s_index

print(ans)

