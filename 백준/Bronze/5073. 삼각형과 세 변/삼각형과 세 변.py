while True:
    a = list(map(int, input().split()))
    a.sort()
    if a[0] == 0 and a[0] == a[1] and a[1] == a[2]:
        break
    elif a[2] >= (a[0] + a[1]):
        print("Invalid")
    elif a[0] == a[2]:
        print("Equilateral")
    elif a[0] == a[1] or a[1] == a[2]:
        print("Isosceles")
    else:
        print("Scalene")