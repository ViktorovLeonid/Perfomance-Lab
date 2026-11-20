import sys
from decimal import Decimal, getcontext


getcontext().prec = 200

with open(sys.argv[1]) as f:
    x, y = map(Decimal, f.readline().split())
    a, b = map(Decimal, f.readline().split())

if a <= 0 or b <= 0:
    raise SystemExit("Радиусы эллипса должны быть больше нуля")

with open(sys.argv[2]) as f:
    for line in f:
        px, py = map(Decimal, line.split())

        value = (px - x) ** 2 * b ** 2 + (py - y) ** 2 * a ** 2
        border = a ** 2 * b ** 2

        if value == border:
            print(0)
        elif value < border:
            print(1)
        else:
            print(2)