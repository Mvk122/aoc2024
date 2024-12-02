def is_increasing(l):
    for i in range(1, len(l)):
        if l[i] - l[i-1] > 0 and l[i] - l[i-1] < 4:
            continue
        return False
    return True

def is_decreasing(l):
    for i in range(1, len(l)):
        if l[i-1] - l[i] > 0 and l[i-1] - l[i] < 4:
            continue
        return False
    return True


def solve():
    safe = 0
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            l = list(map(int, line.split()))
            if is_decreasing(l) or is_increasing(l):
                safe += 1

    return safe

print(solve())