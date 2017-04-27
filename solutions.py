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

# %%

# Question 3
# Given an undirected graph G, find the minimum spanning tree 
# within G. A minimum spanning tree connects all vertices in
# a graph with the smallest possible total weight of edges.
# Your function should take in and return an adjacency list 
# structured like this:
"""    
    {'A': [('B', 2)],
     'B': [('A', 2), ('C', 5)],
     'C': [('B', 5)]}
"""
# Vertices are represented as unique strings.
# The function definition should be `question3(G)`.

                                              
def question3(G):
    min_span_value = 0
    key_values = []
    
    for values in G.values(): # get all values from all keys in one place
        key_values += values
    
    for key in G.keys():
        # print(key)
        temp = 0 # temp value to hold span value
        for value in key_values:
            if key in value:
                if temp == 0: # if no value assigned to temp, assign here
                    temp = value[1]
                    # print(temp)
                elif value[1] < temp: # if value is less than current temp value replace it
                    temp = value[1]
                    # print(temp)    
        min_span_value += temp # add key temp value to minimum span value 
    return min_span_value
                                             

test_dict = {'A': [('B', 2)],
             'B': [('A', 2), ('C', 5)],
             'C': [('B', 5)]}
print(question3(test_dict))

