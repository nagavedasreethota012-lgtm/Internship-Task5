# Problem 14: Anagram
# HackerRank: https://www.hackerrank.com/challenges/anagram/problem

from collections import Counter
for _ in range(int(input())):
    s = input().strip()
    if len(s) % 2:
        print(-1)
    else:
        half = len(s) // 2
        a, b = Counter(s[:half]), Counter(s[half:])
        print(sum((a - b).values()))
