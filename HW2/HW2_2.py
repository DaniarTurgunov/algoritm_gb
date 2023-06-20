class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None

class DoublList:
    def __init__(self):
        self.start_node = None

    def start(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        
    def i_s(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        new_node = Node(data)
        new_node.nref = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node

    def i_e(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref:
            n = n.nref
        new_node = Node(data)
        n.nref = new_node
        new_node.pref = n

    def d_s(self):
        if self.start_node.nref is None:
            self.start_node = None
            return
        self.start_node = self.start_node.nref
        self.start_prev = None

    def d_e(self):
        if self.start_node.nref is None:
            self.start_node = None
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        n.pref.nref = None
    
    def reverse(self):
        p = self.start_node
        q = p.nref
        p.nref = None
        p.pref = q
        while q is not None:
            q.pref = q.nref
            q.nref = p
            p = q
            q = q.pref
        self.start_node = p

    def printList(self):
        n = self.start_node
        while n:
            print(n.item , end = ' ')
            n = n.nref
        print('')

if __name__ == '__main__':
    arr = DoublList()
    arr.start(3)
    arr.i_s(2)
    arr.i_s(1)
    arr.i_e(4)
    arr.i_e(5)
    arr.printList()
    arr.d_e()
    arr.d_e()
    arr.printList()
    arr.reverse()
    arr.printList()