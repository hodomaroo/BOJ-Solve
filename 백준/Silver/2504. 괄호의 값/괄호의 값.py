string = input()
stack,total = [],0
match,multi = {"]" : "[", ")" : "("},{"]" : 3, ")" : 2}

for s in string:
    if s in ("]", ")"):
        if not stack or stack[-1][0] != match[s]:
            print(0)
            exit()

        value = max(1, stack.pop()[1]) * multi[s]
        if stack:
            stack[-1][1] += value
        else:
            total += value
    else:
        stack.append([s, 0])
print(total if not stack else 0)
