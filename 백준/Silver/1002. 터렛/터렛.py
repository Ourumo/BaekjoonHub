# 두 원의 접점의 개수를 출력
import math

t = int(input())
for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    # 0 1 2 -1
    if d == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else: # d > 0
        min_d, max_d = abs(r1 - r2), r1 + r2
        if min_d <= d <= max_d:
            if d == min_d or d == max_d:
                print(1)
            else:
                print(2)
        else:
            print(0)