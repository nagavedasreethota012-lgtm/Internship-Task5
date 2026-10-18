# Problem 7: Alphabet Rangoli
# HackerRank: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def rangoli(size):
    import string

    alphabet = string.ascii_lowercase
    lines = []

    for i in range(size):
        left = [alphabet[size - 1 - j] for j in range(i + 1)]
        right = left[:-1][::-1]
        row = '-'.join(left + right)
        lines.append(row.center(4 * size - 3, '-'))

    return '\n'.join(lines[::-1] + lines[1:])

if __name__ == '__main__':
    n = int(input())
    print(rangoli(n))