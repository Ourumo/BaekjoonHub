a1, a2, a3 = int(input()), int(input()), int(input())
if a1 + a2 + a3 == 180:
    if a1 == a2 and a2 == a3:
        print("Equilateral")
    elif a1 == a2 or a1 == a3 or a2 == a3:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")