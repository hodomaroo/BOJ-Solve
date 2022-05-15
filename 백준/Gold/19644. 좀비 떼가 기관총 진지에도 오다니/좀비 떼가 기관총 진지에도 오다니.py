#--> 어떤 라인의 좀비에게 입힌 피해
#--> (유효사거리 - Ammo Count) * 기관총 공격력
import sys
from collections import deque
input = sys.stdin.readline

L = int(input())
length, damage = map(int,input().split())
ammo = int(input())
zombie = [int(input()) for _ in range(L)]
ammoQueue = deque()

for index, hp in enumerate(zombie):

    while ammoQueue and ammoQueue[0] < (index - length):
        ammoQueue.popleft()

    count = min(index + 1, length) - len(ammoQueue)
    # index + 1이 length보다 크다 --> Lenght회 다 명중 가능
    if count * damage >= hp: #그냥 잡을 수 있는 경우
        continue
    else:
        ammoQueue.append(index)
        ammo -= 1

if ammo < 0:
    print("NO")
else:
    print("YES")


