# Problem 19: Weighted Uniform Strings
# HackerRank: https://www.hackerrank.com/challenges/weighted-uniform-string/problem


def weightedUniformStrings(s, queries):
    weights = set()
    prev = ''
    count = 0

    for ch in s:
        if ch == prev:
            count += 1
        else:
            count = 1
            prev = ch

        weight = (ord(ch) - ord('a') + 1) * count
        weights.add(weight)

    return ['Yes' if q in weights else 'No' for q in queries]


if __name__ == '__main__':
    s = input().strip()
    n = int(input().strip())
    queries = [int(input().strip()) for _ in range(n)]

    result = weightedUniformStrings(s, queries)
    print('\n'.join(result))
