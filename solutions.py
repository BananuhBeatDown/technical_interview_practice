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

# Question 2
# Given a string `a`, find the longest palindromic substring
# contained in `a`. Your function definition should look
# like `question2(a)`, and return a string.

                 
def question2(a):
    if a and len(a) > 1: # determine if `a` is empty or length 1 since both will disqualify
        if len(a) == 2 or len(a) == 3: # exit condition, can't breakdown smaller
            if a[0] == a[-1]: # if first and last characters match return string
                return a
        else:
            if a[0] == a[-1]: # determine if first and last characters match 
                return a[0] + question2(a[1:-1]) + a[-1] # if so, add the character before and after recursion to capture the entire palindrome 
            else:
                return question2(a[1:]) # if not, repeat process using string starting one position from the right
    return None

test_a = ''
print(question2(test_a))
# None 

test_a = 'a'
print(question2(test_a))
# None

test_a = 'aa'
print(question2(test_a))
# aa

test_a = 'ab'
print(question2(test_a))
# None

test_a = 'aba'
print(question2(test_a))
# aba

test_a = 'abab'
print(question2(test_a))
# bab

test_a = 'abcba'
print(question2(test_a))
# abcba
    
test_a = 'cabcba'
print(question2(test_a))
# abcba

