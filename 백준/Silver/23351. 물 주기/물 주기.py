n,k,a,b = map(int, input().split())
mod = n//a #전체 화분에 물 다 주는데 걸리는 시간
day = 0

while (k // mod) > 0:
    k += b - mod
    day += mod
print(day + k)
