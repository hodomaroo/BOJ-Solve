from functools import cmp_to_key

def compare(a : str, b : str) -> int:
    return [1, -1][a + b < b + a]
def compare2(a : str, b : str) -> int:
    a, b = a + frontZero[0], b + frontZero[0]
    return [1, -1][a + b < b + a]
n = int(input())

codes,frontZero = [],[]

for code in input().split():
    if code[0] == "0":
        frontZero.append(code)
    else:
        codes.append(code)


if not codes:
    print("INVALID")
else:
    frontZero.sort(key=cmp_to_key(compare))
    codes.sort(key=cmp_to_key([compare,compare2][len(frontZero) > 0]))
    print(codes[0] + "".join(sorted(codes[1:] + frontZero, key=cmp_to_key(compare))))
    #print("".join()))



