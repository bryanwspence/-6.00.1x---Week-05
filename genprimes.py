#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 12:10:00 2020

@author: bryan.spence
"""

def genPrimes():
    primes = []
    yield primes[0]
    guess = 3
    while True:
        if all(guess%x != 0 for x in primes):
            primes.append(guess)        
        if guess == primes[-1]:
            yield primes[-1]
        guess += 2
