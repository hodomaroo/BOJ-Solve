from collections import Counter

n = int(input())
string = list(input().rstrip())
l,r = 0,0

#startPoint / midPoint / endPoint를 지정
#midPoint ~ endPoint까지는 n종류의 단어가 있는 부분

#startPoint가 바뀌면
# 1 ) midPoint -> 진행하며 n종류가 만족되는 첫 부분을 찾음
# 2 ) endPoint -> len(string)까지 진행하며 n종류가 만족되는 끝부분을 찾음
#like threePointer


endBoolean = [0] * 26 #26가지 알파벳 boolean
endCount = 0
count = 0
#for문 형식으로 진행이 가능!
end = 0
for i in range(len(string)):
    word = ord(string[i]) - ord('a')


    while endCount <= n and end < len(string):  # upperBound?찾기
        #print(i,end)
        endWord = ord(string[end]) - ord('a')
        endCount += not endBoolean[endWord]
        endBoolean[endWord] += 1
        end += 1

    count = max(count,end - i if endCount <= n and end == len(string) else end - i - 1)

    #print(endCount, i, end)
    endBoolean[word] -= 1
    endCount -= not endBoolean[word]
print(count)