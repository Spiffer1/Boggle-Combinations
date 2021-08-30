#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A program to verify that a given string of letters is a possible roll in
a standard game of Boggle.

(This program models the dice in the newer
version of Boggle, sold from 1987 - 2008. See
http://www.bananagrammer.com/2013/10/the-boggle-cube-redesign-and-its-effect.html
for history of the letter distributions used.)

This program stores all combinations of 10 of the dice in a python set, which
is hashed so that membership in the set can be determined quickly. Generating
the set of all combinations of 10 dice takes ~10 seconds on a 2016 MacBook Pro.

After that set is created, any number of Boggle rolls can be checked, requiring
a fraction of a second each. Three test cases are included near the end of
this code.

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

# 3 test cases follow. The first is not a possible roll in Boggle:
roll = 'abcdefghijklmnop'
print(roll, ':', isValidRoll(roll))

roll = 'aaaaacdddeeeeehh'
print(roll, ':', isValidRoll(roll))

roll = 'jsfwttdreyhnsyml'
print(roll, ':', isValidRoll(roll))
