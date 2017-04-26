# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 13:40:27 2017

@author: Matt Green
"""

# Question 1
# Given two strings s and t, determine whether some anagram 
# of t is a substring of s. For example: if s = "udacity" 
# and t = "ad", then the function returns True. Your function 
# definition should look like: question1(s, t) and return a
# boolean True or False.


def question1(s, t):
    index = []
    if not t or not s:
        return False
    elif len(t) > len(s):
        return False
    elif len(t) < 2:
        return False
    for i in t:
        if i not in s:
            return False
        index.append(s.find(i))
    index.sort()
    if index == list(range(index[0], index[-1] + 1)):
        return True
    return False

test_S = 'udacity'
test_T = 'ad'
print(question1(test_S, test_T))

test_S = 'udacity'
test_T = 'aise'
print(question1(test_S, test_T))

test_S = 'udacity'
test_T = 'yadciut'
print(question1(test_S, test_T))

test_S = 'udacity'
test_T = None
print(question1(test_S, test_T))

test_S = 'udacity'
test_T = ''
print(question1(test_S, test_T))

test_S = 'udacity'
test_T = []
print(question1(test_S, test_T))

test_S = 'udacity'
test_T = 'u'
print(question1(test_S, test_T))

test_S = 'u'
test_T = 'ud'
print(question1(test_S, test_T))

# %%