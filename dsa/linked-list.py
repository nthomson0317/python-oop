class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()
    
    def append(self,data):
        new_node = node(data)
        curr = self.head
        while curr.next!=None:
            curr = curr.next
        curr.next = new_node
    
    def length(self):
        curr = self.head
        total = 0
        while curr.next!=None:
            total+=1
            curr = curr.next
        return total
    
    def display(self):
        elems = []
        curr_node = self.head
        while curr_node.next!=None:
            curr_node=curr_node.next
            elems.append(curr_node.data)
        print(elems)