#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 07:05:40 2021

@author: sfottrell
"""


def storeDiceCombinations(depth, combo):
    '''
    Recursive backtracking algorithm to generate a set of all the unique
    letter combinations from the first depth+1 dice. (The first die is #0.)

    combo: list containing the letters in a single combination of dice as
        it is being built up through multiple recursive calls.
    Returns: None. But the method appends to 'combos', a global variable to
        hold the set of all unique letter combinations.
    '''
    global storedCombos
    if depth < 0:
        storedCombos.add(tuple(sorted(combo)))
    else:
        die = dice[depth]
        depth -= 1
        for letter in die:
            combo.append(letter)
            storeDiceCombinations(depth, combo)
            del combo[-1]
        depth += 1


def isValidRoll(roll):
    assert len(roll) == len(dice)
    dieNum = depth + 1
    rollList = list(roll)
    found = False
    return verifyRoll(rollList, dieNum, found)


def verifyRoll(rollList, dieNum, found):
    if dieNum == len(dice):
        if tuple(sorted(rollList)) in storedCombos:
            found = True
    else:
        die = dice[dieNum]
        dieNum += 1
        for letter in die:
            if letter in rollList:
                rollList.remove(letter)
                found = verifyRoll(rollList, dieNum, found)
                rollList.append(letter)
        dieNum -= 1
    return found


dice = [('a', 'e', 'g', 'n'),
        ('a', 'b', 'j', 'o'),
        ('a', 'c', 'h', 'o', 'p', 's'),
        ('a', 'f', 'k', 'p', 's'),
        ('a', 'o', 't', 'w'),
        ('c', 'i', 'm', 'o', 't', 'u'),
        ('d', 'e', 'i', 'l', 'r', 'x'),
        ('d', 'e', 'l', 'r', 'v', 'y'),
        ('d', 'i', 's', 't', 'y'),
        ('e', 'g', 'h', 'n', 'w'),
        ('e', 'i', 'n', 's', 'u'),
        ('e', 'h', 'r', 't', 'v', 'w'),
        ('e', 'i', 'o', 's', 't'),
        ('e', 'l', 'r', 't', 'y'),
        ('h', 'i', 'm', 'n', 'u', 'q'),
        ('h', 'l', 'n', 'r', 'z')]


# Create a set of all possible letter combinations from the first 10 dice.
depth = 9
storedCombos = set()
combo = []
storeDiceCombinations(depth, combo)
print('Combinations stored')

# roll = 'abcdefghijklmnop'
# roll = 'aaaaacdddeeeeehh'
roll = 'ejsfttdryhnwsyml'
print(isValidRoll(roll))
