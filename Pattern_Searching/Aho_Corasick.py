# -*- coding: utf-8 -*-
"""
@author: Abdullah
@Email: abdullah.khan230@yahoo.com
@Github: https://github.com/Abdullah230
Created on Sun Apr 12 21:48:02 2020
"""
#Trees will use methods to use Nodes
def get_key(val, dictionary):
    for key, value in dictionary.items():
        if value == val:
            return key

class tree:
    def __init__(self):
        self.treeList = []
        self.nodes = 0
        self.o = []
        self.alphabets = []
        return
    
    def append_words(self,words):
        k = 0
        for word in words:
            j = 0
            for i in range(len(word)):
                if self.nodes == 0:
                    self.treeList.append(Node(self.nodes, ''))
                    self.nodes += 1
    
                if len(self.treeList[0].children) == 0:
                    self.treeList.append(Node(self.nodes, word[i]))
                    ph = Node(self.nodes, word[i])
                    self.treeList[0].attach_node(ph)
                    self.nodes += 1
                    j += 1
                    if i == (len(word) - 1):
                        self.treeList[j].end.append(k+1)
                    
                else:
                    if word[i] in self.treeList[j].children.values():
                        j = get_key(word[i], self.treeList[j].children)
                    else:
                        self.treeList.append(Node(self.nodes, word[i]))
                        ph = Node(self.nodes, word[i])
                        self.treeList[j].attach_node(ph)
                        j = self.nodes
                        self.nodes += 1
                        
                    
                    if i == len(word) - 1:
                        self.treeList[j].end.append(k+1)
            k += 1          
        
        for i in range(len(self.treeList) - 1):
            if len(self.treeList[i+1].end) == 0:
                self.o.append(0)
            else:
                self.o.append(self.treeList[i+1].end[0])
        
        for word in words:
            for i in range(len(word)):
                if word[i] not in self.alphabets:
                    self.alphabets.append(word[i])
        
        for i in range(len(self.treeList)):
            print(self.treeList[i].parent)
        
        return            
#        for i in range(len(self.treeList) - 1):
#            temp = []
#            j = self.treeList[i+1].number
#            while self.treeList[j].parent != 0:
#                
#                

        
# Nodes are just structures
class Node:
    def __init__(self, number, letter):
        self.children = {}
        self.parent = 0
        self.number = number
        self.letter = letter
        self.end = []
        self.f = []
        
    def attach_node(self,Node):
        self.children[Node.number] = Node.letter
        Node.parent = self.number
        
    
# f will define where to jump in case of a failure
# O will define the ouput
