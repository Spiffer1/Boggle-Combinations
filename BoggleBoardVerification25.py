#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A program to verify that a given string of letters is a possible roll in
a standard game of Boggle.

(This program models the dice in the original version of Big Boggle.
See the letter distributions on the last post (from Dean Howard) in this
thread, e.g.:
for history of the letter distributions used.)
https://boardgamegeek.com/thread/300883/letter-distribution

This program stores all combinations of 11 of the dice in a python set, which
is hashed so that membership in the set can be determined quickly. Generating
the set of all combinations of 11 dice takes ~10 seconds on a 2016 MacBook Pro.

After that set is created, any number of Boggle rolls can be checked, typically
requiring between 1 and 60 seconds each. Several test cases are included at
the end of this code.

Created on Wed Aug 25 07:05:40 2021

@author: sfottrell
"""


import random


def storeDiceCombinations(depth, combo):
    '''
    Recursive backtracking algorithm to generate a set of all the unique
    letter combinations from the first depth+1 dice. (The first die is #0.)

    combo: list containing the letters in a single combination of dice as
        it is being built up through multiple recursive calls.
    Returns: None. But the method appends to 'storedCombos', a global variable
        to hold the set of all unique letter combinations.
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
    '''
    Sets up necessary variables for the recursive algorithm verifyRoll().

    roll: String. Letters in a Boggle dice roll that will be tested.
    '''
    assert len(roll) == len(dice)
    currentDie = numStoredDice
    rollList = list(roll)
    found = False
    return verifyRoll(rollList, currentDie, found)


def verifyRoll(rollList, currentDie, found):
    '''
    Recursive backtracking algorithm to determine whether the letters in
    rollList could really be produced by the 25 dice.

    rollList: letters from a roll String converted to a list
    currentDie: tuple of letters from one die (one element of dice)
    found: boolean set to True once a roll has been verified

    With each call to verifyRoll(), the next "currentDie" is selected. Each
    letter from the die is tested: if that letter is contained within rollList,
    it is temporarily removed from rollList and a new call to verifyRoll will
    select the next "currentDie". Once all dice (beyond those that were stored)
    have been verified, the remaining letters in the rollList are checked
    against the combinations stored in the hash.
    '''
    if currentDie == len(dice):
        if tuple(sorted(rollList)) in storedCombos:
            found = True
    else:
        die = dice[currentDie]
        currentDie += 1
        for letter in die:
            if letter in rollList:
                rollList.remove(letter)
                found = verifyRoll(rollList, currentDie, found)
                rollList.append(letter)
        currentDie -= 1
    return found


dice = [('a', 'f', 'r', 's'),
        ('a', 'e'),
        ('a', 'f', 'i', 'r', 's'),
        ('a', 'd', 'e', 'n'),
        ('a', 'e', 'm'),
        ('a', 'e', 'g', 'm', 'u'),
        ('a', 'e', 'g', 'm', 'n'),
        ('a', 'f', 'i', 'r', 's', 'y'),
        ('b', 'j', 'k', 'q', 'x', 'z'),
        ('c', 'e', 'n', 's', 't'),
        ('c', 'e', 'i', 'l', 't'),
        ('c', 'e', 'i', 'p', 's', 't'),
        ('d', 'h', 'n', 'o', 't'),
        ('d', 'h', 'l', 'o', 'r'),
        ('d', 'h', 'l', 'o', 'r'),
        ('d', 'h', 'l', 'n', 'o', 'r'),
        ('e', 'i', 't'),
        ('c', 'e', 'i', 'l', 'p', 't'),
        ('e', 'm', 'o', 't'),
        ('e', 'n', 's', 'u'),
        ('f', 'i', 'p', 'r', 's', 'y'),
        ('g', 'o', 'r', 'v', 'w'),
        ('i', 'p', 'r', 'y'),
        ('n', 'o', 't', 'u', 'w'),
        ('o', 't', 'u')]


# Create a set of all possible letter combinations from the first 11 dice.
numStoredDice = 11
depth = numStoredDice - 1  # the 0-indexed diceNumber for recursion
storedCombos = set()
combo = []
storeDiceCombinations(depth, combo)
print('Combinations stored')

# Test cases follow. The first is not a possible roll in Boggle:
roll = 'abcdefghijklmnopqrstuvwxy'
print(roll, ':', isValidRoll(roll))

roll = 'aaaaaaaabcccddddeceefgino'
print(roll, ':', isValidRoll(roll))

# I picked this "randomly" by selecting one letter off each die.
# Random selections often take a fairly long time to verify.
roll = 'raidaenfxciehorltpossrptu'
print(roll, ':', isValidRoll(roll))

roll = 'saioftnteetrshehlaateadij'
print(roll, ':', isValidRoll(roll))

roll = 'eseiadrtsrtageaplintxsesi'
print(roll, ':', isValidRoll(roll))

# False: this contains the maximum number of 'i's (6) and also has 2 'f's.
# But 3 of the 4 'f's occur on dice that also have 'i's. So you can't
# get 6 'i's AND 2 'f's.
roll = 'eseiadrtsrtiiiaffintxsesi'
print(roll, ':', isValidRoll(roll))

# Chooses a truly random letter off each die and then shuffles the order.
roll = ''
for die in dice:
    roll += random.choice(die)
roll = ''.join(random.sample(roll, len(roll)))
print(roll, ':', isValidRoll(roll))
