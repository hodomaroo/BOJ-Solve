values = [input() for _ in range(int(input()))]
for i in range(len(values[0])):
    if len(set(value[i] for value in values)) == 1:
        print(values[0][i],end = "")
    else:
        print("?", end = "")