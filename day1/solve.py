from collections import Counter

def solve():
    left = []
    right = []
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            l, r = line.split()
            left.append(int(l))
            right.append(int(r))

    left.sort()
    right.sort()

    ans = 0
    for l, r in zip(left, right):
        ans += abs(l-r)

    return ans

def solve_second():
    left = []
    right = []
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            l, r = line.split()
            left.append(int(l))
            right.append(int(r))

    r_counts = Counter(right)

    total = 0
    for l in left: 
        if l in r_counts:
            total += l * r_counts[l]

    return total

    

if __name__ == "__main__":
    print(solve_second())