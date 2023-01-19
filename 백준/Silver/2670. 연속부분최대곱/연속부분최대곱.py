from itertools import accumulate
print("%.3f" % max(list(accumulate(list(float(input()) for _ in range(int(input()))), lambda prev,cur : max(prev * cur, cur)))))