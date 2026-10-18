# Problem 13: Sherlock and the Valid String
# HackerRank: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem


from collections import Counter

def isValid(s):
    freq = Counter(Counter(s).values())

    if len(freq) == 1:
        return "YES"

    if len(freq) == 2:
        f1, f2 = freq.keys()
        c1, c2 = freq.values()

        if (f1 == 1 and c1 == 1) or (f2 == 1 and c2 == 1):
            return "YES"

        if abs(f1 - f2) == 1 and (c1 == 1 or c2 == 1):
            return "YES"

    return "NO"


if __name__ == '__main__':
    s = input().strip()
    print(isValid(s))
