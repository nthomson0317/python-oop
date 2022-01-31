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
    
    def get(self,index):
        if index>=self.length():
            print("ERROR: 'Get' index out of range!")
            return None
        else:
            cur_idx = 0
            cur_node = self.head
            while True:
                cur_node = cur_node.next
                if cur_idx==index:
                    return cur_node.data
                cur_idx+=1
    
my_list = linked_list()

my_list.display()
#[]

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.display()
#[1, 2, 3, 4]

print("element at 2nd index: %d" % my_list.get(2))
#element at 2nd index: 3

