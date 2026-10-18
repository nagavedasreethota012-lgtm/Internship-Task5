# Problem 12: Making Anagrams
# HackerRank: https://www.hackerrank.com/challenges/making-anagrams/problem


from collections import Counter

def makingAnagrams(s1, s2):
    count1 = Counter(s1)
    count2 = Counter(s2)

    deletions = 0

    for char in set(s1) | set(s2):
        deletions += abs(count1[char] - count2[char])

    return deletions


if __name__ == '__main__':
    s1 = input().strip()
    s2 = input().strip()

    print(makingAnagrams(s1, s2))
