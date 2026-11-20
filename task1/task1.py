import sys


def make_path(n, m):
    path = []
    current = 0

    while True:
        path.append(current + 1)
        current = (current + m - 1) % n

        if current == 0:
            break

    return path


n1, m1, n2, m2 = map(int, sys.argv[1:5])

path1 = make_path(n1, m1)
path2 = make_path(n2, m2)

print(''.join(map(str, path1 + path2)))