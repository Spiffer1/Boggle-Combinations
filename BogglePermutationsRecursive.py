#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 07:05:40 2021

@author: sfottrell
"""


from timeit import default_timer as timer


def findAllCombinations(depth, combo):
    global combos
    if depth < 0:
        combos.add(tuple(sorted(combo)))
    else:
        die = dice[depth]
        depth -= 1
        for letter in die:
            combo.append(letter)
            findAllCombinations(depth, combo)
            del combo[-1]
        dice.append(die)
        depth += 1


dice = [('a', 'f', 'r', 's'),
        ('a', 'e'),
        ('a', 'f', 'i', 'r', 's'),
        ('a', 'd', 'e', 'n'),
        ('a', 'e', 'm'),
        ('a', 'e', 'g', 'm', 'u'),
        ('a', 'e', 'g', 'm', 'n'),
        ('a', 'f', 'i', 'r', 's', 'y'),
        ('b', 'j', 'k', 'Q', 'x', 'z'),
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


# depth = len(dice) - 1
times = []
numCombos = []
print("# of Dice   Number of combinations   Time to calculate")

for depth in range(1, len(dice)):
    combos = set()
    combo = []
    start = timer()
    findAllCombinations(depth, combo)
    end = timer()
    time = end - start
    times.append(time)
    numCombos.append(len(combos))
    print(depth, len(combos), time)

print(numCombos)
