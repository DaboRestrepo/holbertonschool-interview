#!/usr/bin/python3
"""This modulo soport the prime game function"""


def isWinner(x, nums):
    """Define the winner"""
    if not nums or x < 1:
        return None
    n = max(nums)
    list = [True for _ in range(max(n + 1, 2))]
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not list[i]:
            continue
        for j in range(i*i, n + 1, i):
            list[j] = False

    list[0] = list[1] = False
    c = 0
    for i in range(len(list)):
        if list[i]:
            c += 1
        list[i] = c

    player1 = 0
    for n in nums:
        player1 += list[n] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
