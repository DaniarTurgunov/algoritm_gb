class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def append(self, val):
        end = Node(val)
        n = self
        while (n.next):
            n = n.next
        n.next = end

def printList(head):
    ptr = head
    while ptr:
        print(ptr.data, end = ' ')
        ptr = ptr.next
    print('')

def reverse(head):
    previous = None
    current = head
    while current:
        next = current.next
        current.next = previous       
        previous = current
        current = next
    return previous
 
if __name__ == '__main__':
    head = Node(1)
    head.append(2)
    head.append(3)
    printList(head)

    head = reverse(head)
    printList(head)