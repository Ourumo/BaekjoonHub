import sys

N = int(sys.stdin.readline())
meetings = []
count, last_time = 0, 0

for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    meetings.append([start, end])

meetings.sort(key=lambda x: (x[1], x[0]))

for s, e in meetings:
    if s >= last_time:
        count += 1
        last_time = e

print(count)