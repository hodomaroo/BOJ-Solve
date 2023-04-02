from itertools import product

states = [[v == 'O' for v in list(input())] for _ in range(10)]


def judge(action_of_first_row: list[int]) -> int:
    _count, copied_states = 0, [v[:] for v in states]
    # stack = []
    for i in range(10):
        for j in range(10):
            if (not i and action_of_first_row[j]) or (i and copied_states[i-1][j]):
                _count += 1
                if i:  # 상
                    copied_states[i-1][j] = not copied_states[i-1][j]
                if j:  # 좌
                    copied_states[i][j - 1] = not copied_states[i][j - 1]
                if j != 9:  # 우
                    copied_states[i][j + 1] = not copied_states[i][j + 1]
                if i != 9:  # 하
                    copied_states[i + 1][j] = not copied_states[i + 1][j]

                copied_states[i][j] = not copied_states[i][j]

    return 101 if sum(copied_states[-1]) else _count


_ans = 101
for _case in product((False, True), repeat=10):

    _ans = min(judge(_case), _ans)

print(_ans if _ans != 101 else -1)
