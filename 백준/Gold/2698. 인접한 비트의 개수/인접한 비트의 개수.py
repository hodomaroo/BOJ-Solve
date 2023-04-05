from functools import lru_cache


# 길이가 a인, 1이 b개 나온, 끝이 c인 경우의 수
# dp[a][b][c]
# baseCase ->
# dp[0][0][0 / 1] = 1
# dp[~][0][0] = 1

# mode -> 0 : 0 / 1 : 1 / 2 : both
@lru_cache(None)
def get_case(remainLen: int, remainAdj: int, mode: int):
    if not remainLen and not remainAdj:
        return 1

    _count = 0
    # 0으로
    if mode:
        for i in range(1, remainLen - remainAdj + (not remainAdj)):
            _count += get_case(remainLen - i, remainAdj, 0)

    # 1으로
    if mode in (0, 2):
        for i in range(1,  min(remainLen + 1, remainAdj + 2)):  # 1의 개수
            _count += get_case(remainLen - i, remainAdj - (i - 1), 1)

    return _count


for i in range(int(input())):
    n, k = map(int, input().split())
    print(get_case(n, k, 2))


# 4 1
# 1101
# 0110
# 0011
# 1011
