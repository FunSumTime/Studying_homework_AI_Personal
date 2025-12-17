class Node:
    def  __init__(self,value):
        self.value = value
        self.next = None

class  LinkedList:
    def __init__(self):
        self.head = None
    
    def  append(self,value):
        if self.head:
            current = self.head
            while current.next:
                current  =  current.next
            # want  to change current.next  to mess  with memroy not  just a varable
            current.next = Node(value)
            
        else:
            self.head = Node(value)
    def  print_list(self):
        curr = self.head
        while  curr:
            print(curr.value, end=" -> ")
            curr  =  curr.next
        print("None")


ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.print_list()
