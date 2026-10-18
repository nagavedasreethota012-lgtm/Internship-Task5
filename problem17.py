# Problem 17: Separate the Numbers
# HackerRank: https://www.hackerrank.com/challenges/separate-the-numbers/problem


def separateNumbers(s):
    n = len(s)

    for length in range(1, n // 2 + 1):
        first = s[:length]

        # Numbers cannot have leading zeros
        if first[0] == '0':
            continue

        current = int(first)
        expected = first

        while len(expected) < n:
            current += 1
            expected += str(current)

        if expected == s:
            print("YES", first)
            return

    print("NO")


if __name__ == '__main__':
    q = int(input().strip())

    for _ in range(q):
        s = input().strip()
        separateNumbers(s)
