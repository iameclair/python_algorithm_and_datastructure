'''
Created on Oct 5, 2017

@author: Eclair Lumu
'''
from linkedlist.Node import Node;

class LinkedList(object):
    
    #when the list is instantiated the head is set to none
    def __init__(self, head=None):
        self.head = head;
        
    #insert a new node at the top of the list
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        
    def size(self):
        current = self.head
        count = 0
        
        while current:
            count +=1
            current = current.get_next()
            
        return count
     
        
    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
                
            else:
                current = current.get_next()
            
            if current is None:
                raise ValueError('Linked list is empty')
            
        return current
    
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        
        if current is None:
            raise ValueError('List is empty')
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
            
    