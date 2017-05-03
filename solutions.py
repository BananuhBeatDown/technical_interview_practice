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
    if t and s: # Not empty?
        if len(t) >= 2: # no one letter palindromes
            while len(s) >= len(t): # t is subset of s
                verify = 0 
                for c in set(t): # only unique characters
                    if t.count(c) == s[:len(t)].count(c): # compare char counts between t and s snippet
                        verify += t.count(c) # Add the char count to verify if t same char count as s
                if verify == len(t): # if all characters match verfiy and len(t) will be the same size
                    return True
                s = s[1:] # if not palindrome try again with the next iteration of s one char forward
    return False

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
# False

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
    return


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


def edges_parent_rank(G):
    edges = []
    parent = {}
    rank = {}
    for key in G.keys():
        parent[key] = key
        rank[key] = 0
        for value in G[key]:
            edges.append((value[1], key, value[0]))
    edges.sort()
    for i in range(len(edges) - 1):
        j = 1
        prev_len = len(edges)
        while len(edges) == prev_len:
            if i + j > len(edges) - 1:
                break
            if edges[i][0] in edges[i+j]:
                if edges[i][1] in edges[i+j] and edges[i][2] in edges[i+j]:
                    del edges[i + j]
                else:
                    j += 1
    return edges, parent, rank


def question3(G):
    if G:
        
        def find(vert):
            if parent[vert] != vert:
                parent[vert] = find(parent[vert])      
            return parent[vert]
            
        def union(vert1, vert2):
            if find(vert1) != find(vert2):
                if rank[vert1] <= rank[vert2]:
                    rank[vert2] += 1
                    parent[find(vert1)] = find(vert2)
                else:
                    parent[find(vert2)] = find(vert1)
                    rank[vert1] += 1                          
        
        min_span_tree = set()
        edges, parent, rank = edges_parent_rank(G)
#        print(edges)
#        print('')
        for weight, vert1, vert2 in edges:
#            print(rank)
            # print(len(min_span_tree), len(edges) - 1)
#            print(vert1, vert2)
#            print(find(vert1), find(vert2))
#            print(rank[find(vert1)], rank[find(vert2)])
#            print([parent])
#            print('')
            if len(min_span_tree) != len(G) - 1:
                if find(vert1) != find(vert2):
                    min_span_tree.add((weight, vert1, vert2))
                    union(vert1, vert2)
    #                print((weight, vert1, vert2))
    #                print('')
                else:
                    next
                
        G = G.fromkeys(G, [])
        for key in G:
            edges = []
            for edge in min_span_tree:
                if key == edge[1]:
                    edges.append((edge[2], edge[0]))
                else:
                    if key == edge[2]:
                        edges.append((edge[1], edge[0]))
                    else:
                        next
            G[key] = edges
        return G
    return            
            

test_dict = {'A': [('B', 2), ('D', 1)],
             'B': [('A', 2), ('C', 5), ('D', 1)],
             'C': [('B', 5), ('D', 3)],
             'D': [('A', 1), ('C', 3), ('B', 1)]
             }
print(question3(test_dict))
# {'A': [('D', 1)],
#  'B': [('D', 1)],
#  'C': [('D', 3)],
#  'D': [('C', 3), ('B', 1), ('A', 1)]
# }


test_dict = {}
print(question3(test_dict))
# None

test_dict = {'A': [('B', 4), ('H', 8)],
             'B': [('A', 4), ('C', 8), ('H', 11)],
             'C': [('B', 8), ('D', 7), ('F', 4), ('I', 2)],
             'D': [('C', 7), ('E', 9), ('F', 14)],
             'E': [('D', 9), ('F', 10)],
             'F': [('E', 10), ('D', 14), ('C', 4), ('G', 2)],
             'G': [('F', 2), ('I', 6), ('H', 1)],
             'H': [('G', 1), ('I', 7), ('A', 8), ('B', 11)],
             'I': [('H', 7), ('C', 2), ('G', 6)]      
             }
print(question3(test_dict))
# {'A': [('B', 4), ('H', 8)],
#  'B': [('A', 4)],
#  'C': [('F', 4), ('I', 2), ('D', 7)], 
#  'H': [('A', 8), ('G', 1)],
#  'E': [('D', 9)],
#  'F': [('C', 4), ('G', 2)], 
#  'I': [('C', 2)], 
#  'D': [('C', 7), ('E', 9)], 
#  'G': [('F', 2), ('H', 1)]
#  }

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
                    return
            else: # if two branches in recursive step try first branch then second if first fails
                try:
                    if question4one(T, T[r].index(1), n) > -1:
                        return r
                except:
                    try:
                        if question4one(T, T[r].index(1, 2), n) > -1:
                            return r
                    except: # if second fails return none
                        return
    return


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
            return
        while counter <= position:
            if counter == position:
                return current.data
            current = current.next
            counter += 1
        return
    
    def get_len(self): # return length of list
        counter = 1 # start count at 1 not 0
        current = self.head
        while current.next:  # when current.next is not none return current
            current = current.next
            counter += 1
        return counter


def question5(ll, m):
    if m <= ll.get_len() and m > -1: # check if m is out of index of or a negative number
        if ll.get_len() - m == 0:
            return ll.head.data
        return ll.get_position(ll.get_len() - m + 1)
    return      


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

ll = LinkedList(n1)
ll.append(n2)
ll.append(n3)
ll.append(n4)

print(ll.get_len())
# 4

print(ll.get_position(3))
# 3

print(question5(ll, 2))
# 3

print(question5(ll, 3))
# 2

print(question5(ll, 5))
# None

print(question5(ll, 1))
# 4

print(question5(ll, 4))
# 1

