'''
Created on Oct 5, 2017

@author: Eclair Lumu
'''
from linkedlist.LinkedList import LinkedList

#instantiate
linkedList = LinkedList();

linkedList.insert(8)
linkedList.insert(5)
linkedList.insert(12)
linkedList.insert(9)
linkedList.insert(11)

print('Insert print linked list')
linkedList.traverseList()

linkedList.remove(5)
print('Remoove print linked list')
linkedList.traverseList()
