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
    if t and s:
        if len(t) <= len(s):
            if len(t) >= 2: 
                for p in permutations(t):
                    if p in s:
                        return True
                return False
                        
def permutations(s):
    if len(s) == 1:
        return s
    recursive_perms = set()
    for c in s:
        for perm in permutations(s.replace(c,'',1)):
            recursive_perms.add(c+perm)
    return recursive_perms

test_S = 'bccbba'
test_T = 'abc'
print(question1(test_S, test_T))
# False

test_S = 'udacity'
test_T = 'ad'
print(question1(test_S, test_T))
# True

test_S = 'udacity'
test_T = 'aise'
print(question1(test_S, test_T))
# False

test_S = 'udacity'
test_T = 'yadciut'
print(question1(test_S, test_T))
# True

test_S = 'udacity'
test_T = None
print(question1(test_S, test_T))
# False

test_S = 'udacity'
test_T = ''
print(question1(test_S, test_T))
# False

test_S = 'udacity'
test_T = []
print(question1(test_S, test_T))
# False

test_S = 'udacity'
test_T = 'u'
print(question1(test_S, test_T))
# False

test_S = 'bbcba'
test_T = 'abc'
print(question1(test_S, test_T))
# True

test_S = 'u'
test_T = 'ud'
print(question1(test_S, test_T))


# %%

def question1(s, t):
    index = {}
    if t and s:
        if len(t) <= len(s):
            if len(t) >= 2:
                for i in set(t):
                    if i not in s:
                        return False
                    else:
                        index[i] = s.count(i)
                return index
    return False
                         

test_S = 'bccbba'
test_T = 'abc'
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
# 9


test_dict = {}


print(question3(test_dict))
# 0


test_dict = {'A': [('B', 5), ('C', 2)],
             'B': [('A', 2), ('C', 5)],
             'C': [('A', 5), ('B', 2)]}
print(question3(test_dict))
# 6

# %%

# Question 4
# Find the least common ancestor between two nodes on a binary search tree.
# The least common ancestor is the farthest node from the root that is an
# ancestor of both nodes. For example, the root is a common ancestor. You
# can assume that both nodes are in the tree, and the tree itself adheres
# to all BST properties. The function definition should look like
# `question4(T, r, n1, n2)`, where `T` is the tree represented as a matrix,
# where the index of the list is equal to the integer stored in that node and
# and a `1` representing a child node, `r` is a non-negative integer
# representing the root, and `n1` and `n2` are non-negative integers
# representing the two nodes in no particular order.


def question4(T, r, n1, n2):
    if T and T[0]:
        if sum(T[r]) == 1:
              if T[r][n1] or T[r][n2]:
                  return None
              return question4(T, T[r].index(1), n1, n2)
        else: 
            if question4one(T, r, n1) and question4one(T, r , n2):
                return r
        return None


def question4one(T, r, n): # Test to see if n is in branch
    if sum(T[r]): 
        if T[r][n]: # if branch is in initial node return r and were done
            return r
        else:
            if sum(T[r]) == 1: # if only one branch run recursive step
                try:
                    if question4one(T, T[r].index(1), n) > -1:
                        return r
                except: # if branch node is empty return none
                    return None
            else: # if two branches in recursive step try first branch then second if first fails
                try:
                    if question4one(T, T[r].index(1), n) > -1:
                        return r
                except:
                    try:
                        if question4one(T, T[r].index(1, 2), n) > -1:
                            return r
                    except: # if second fails return none
                        return None
    return None


test_matrix = [[0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [1, 0, 0, 0, 1],
               [0, 0, 0, 0, 0]]
print(question4(test_matrix, 3, 1, 4))
# 3

test_matrix = [[0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0]]
print(question4(test_matrix, 3, 1, 4))
# None


test_matrix = [[0, 0, 0, 0, 0],
               [1, 0, 0, 0, 1],
               [0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0]]
print(question4(test_matrix, 3, 1, 4))        
# None


test_matrix = [[0, 0, 0, 0, 0],
               [1, 0, 0, 0, 1],
               [0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0]]
print(question4(test_matrix, 3, 0, 4))
# 1


test_matrix = [[0, 0, 0, 0, 1],
               [1, 0, 0, 1, 0],
               [0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0]]
print(question4(test_matrix, 3, 0, 4))
# 1


test_matrix = [[0, 0, 0, 0, 1],
               [0, 0, 1, 1, 0],
               [1, 0, 0, 0, 0],
               [0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0]]
print(question4(test_matrix, 3, 0, 4))
# 1


test_matrix = [[0, 0, 0, 0, 1],
               [0, 0, 1, 1, 0],
               [0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0],
               [0, 0, 0, 0, 0]]
print(question4(test_matrix, 3, 0, 4))
# None


test_matrix =   [[0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0]]
print(question4(test_matrix, 3, 2, 5))
# 1


test_matrix = []
print(question4(test_matrix, 3, 2, 5))
# None


test_matrix = [[]]
print(question4(test_matrix, 3, 2, 5))
# None

# %%

# Question 5
# Find the elemnet in a singly linked list that's `m` elements from the end.
# For example, if a linked list has 5 elements, the 3rd element from the end
# is the 3rd element. The function definition should look like `question5(ll, m)`,
# where `ll` is the first node of a linked list and `m` is the "mth number from
# the end". Return the value of the node at that position.


class Node(object): # create the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object): # create a linked list object
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_node): # add a method to add item to end of list
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
            
    def get_position(self, position): # return node value from requested position in list 
        counter = 1
        current = self.head
        if position < 1 or position > ll.get_len(): # check for real position and not out of list index
            return None
        while counter <= position:
            if counter == position:
                return current.data
            current = current.next
            counter += 1
        return None
    
    def get_len(self): # return length of list
        counter = 1 # start count at 1 not 0
        current = self.head
        while current.next != None:  # when current.next is not none return current
            current = current.next
            counter += 1
        return counter


def question5(ll, m):
    if m <= ll.get_len() and m > -1: # check if m is out of index of or a negative number
        return ll.get_position(ll.get_len() - m + 1)
    return None       


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

ll = LinkedList(n1)
ll.append(n2)
ll.append(n3)
ll.append(n4)


print(question5(ll, 2))
# 2

print(question5(ll, 5))
# None

print(question5(ll, 4))
# 4
