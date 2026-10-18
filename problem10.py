# Problem 10: CamelCase
# HackerRank: https://www.hackerrank.com/challenges/camelcase/problem

s = input().strip()
print(1 + sum(char.isupper() for char in s) if s else 0)
