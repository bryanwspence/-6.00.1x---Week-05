#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 09:12:53 2020

@author: bryan.spence
"""


    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''        
        hand_keys = sorted(self.hand.keys())
        for letter in hand_keys:
            for j in range(self.hand[letter]):
                output += letter
        return output