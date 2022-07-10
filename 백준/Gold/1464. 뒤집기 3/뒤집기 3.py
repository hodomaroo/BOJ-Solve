from collections import deque
string = input()
Min = ["_" * i for i in range(len(string))]
RvMin = ["_" * i for i in range(len(string))]
Min[0] = string[0]
RvMin[0] = string[0]

for i in range(len(string)-1):
    a,b,c,d = Min[i] + string[i + 1], RvMin[i] + string[i + 1], Min[i][::-1] + string[i + 1], RvMin[i][::-1] + string[i + 1]

    Min[i + 1] = min(a,b,c,d)
    RvMin[i + 1] = min(a[::-1], b[::-1],c[::-1],d[::-1])[::-1]
print(min(Min[-1],RvMin[-1][::-1]))




