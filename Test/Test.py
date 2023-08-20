class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

t = Node("t")

#TODO: Remove only the first instance of target value AND redirect node.next
#

def algorithm(list1, target):
    prev = None
    curr = list1

    if curr.next is None:
        return None

    while curr:
        if curr.val == target and prev is None:
            list1 = list1.next
            return list1        
        elif curr.val == target:
            prev.next = curr.next
            return list1
        prev = curr
        curr = curr.next

list1 = algorithm(t, "t")
while list1:
    print(list1.val)
    list1 = list1.next

#TODO: Left off at 03:40 on design requirements (system architecture)