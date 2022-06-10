from heapq import heappop,heappush,heapify


stringHeap = [input() + "_" for _ in range(int(input()))]
heapify(stringHeap)
ans = []
while stringHeap:
    string = heappop(stringHeap)
    ans.append(string[0])
    if len(string) > 2:
        heappush(stringHeap, string[1:])
print("".join(ans))

#front -> 제일 높은 우선순위
#second -> 두번째...
#두 문자열의 길이가 다른 경우 ->
#-> BA / BAC
#둘의 우선순위가 같다면 길이가 긴걸 선택한다!

# BA BAA BAAA #--> 가장 효율성이 높게 진행할수 있도록 생각해본다?