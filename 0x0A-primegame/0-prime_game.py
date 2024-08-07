#!/usr/bin/python3
""" Prime game module """


def isWinner(x, nums):
    """ Return: Winner"""
    if not nums or x < 1:
        return None
    highNum = max(nums)

    figrs = [True for _ in range(max(highNum + 1, 2))]
    for v in range(2, int(pow(highNum, 0.5)) + 1):
        if not figrs[v]:
            continue
        for k in range(v * v, highNum + 1, v):
            figrs[k] = False
    figrs[0] = figrs[1] = False
    primeInt = 0
    for v in range(len(figrs)):
        if figrs[v]:
            primeInt += 1
        figrs[v] = primeInt
    maria_Wns = 0
    for x in nums:
        maria_Wns += figrs[x] % 2 == 1
    if maria_Wns * 2 == len(nums):
        return None
    if maria_Wns * 2 > len(nums):
        return "Maria"
    return "Ben"
