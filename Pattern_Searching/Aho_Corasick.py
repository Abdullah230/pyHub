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
    def __init__(self,tree):
        self.treeList = []
        self.nodes = 0
    
        
    def append_node(self,word):
        i = 0
        j = 0
        if self.nodes == 0:
            self.treeList.append(Node(self.nodes+1, word[i]))
        
        else:
            if len(self.treeList[0].children) == 0:
                self.treeList[0].attach_node(Node(self.nodes+1, letter))
                
            else:
                while  in self.treeList[i].children.values():
                    i = get_key(letter, self.treeList[i].children)
                
        

        
# Nodes are just structures
class Node:
    
    def __init__(self, number, letter):
        self.children = {}
        self.parent = 0
        self.number = number
        self.letter = letter
        
    def attach_node(self,Node):
        self.children[Node.number] = Node.letter
        Node.parent = self.number
        
    
# f will define where to jump in case of a failure
# O will define the ouput