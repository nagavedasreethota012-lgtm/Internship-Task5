# Problem 16: Caesar Cipher
# HackerRank: https://www.hackerrank.com/challenges/caesar-cipher-1/problem


def caesarCipher(s, k):
    result = []
    k %= 26

    for ch in s:
        if 'a' <= ch <= 'z':
            result.append(chr((ord(ch) - ord('a') + k) % 26 + ord('a')))
        elif 'A' <= ch <= 'Z':
            result.append(chr((ord(ch) - ord('A') + k) % 26 + ord('A')))
        else:
            result.append(ch)

    return ''.join(result)


if __name__ == '__main__':
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())

    print(caesarCipher(s, k))
