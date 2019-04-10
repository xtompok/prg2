class ListNode(object):

    def __init__(self,data):
        super(ListNode,self).__init__()
        self.data = data
        self.next = None



class LinkedList(object):
    def __init__(self):
        super(LinkedList,self).__init__()
        self.head = None

    def append(self,data):
        if self.head is None:
            self.head = ListNode(data)
            return

        act = self.head
        while act.next is not None:
            act = act.next

        new_node = ListNode(data)
        act._next = new_node

    def show(self):
        """Vytiskne jednotlivé prvky seznamu"""
        if self.head is None:
        #    self.head = ListNode(data)
        #   seznam je prazdny
            return

        act = self.head
        while act.next is not None:
            # vytisknu hodnotu act
            act = act.next
        print("Prvek: {}".format(act.data))

    def insert(self,idx,data):
        """Vloží na pozici idx prvek obsahující data,
           ostatní odsune."""

        # Dojdu na (idx-1). prvek
        # Vytvořím nový prvek obsahující data
        # odkaz next z (idx-1). prvku přesměruji na nový prvek
        # odkaz z nového prvku přesměruji na (původně) i. prvek

ll = LinkedList()
ll.show()
ll.append(3)
ll.show()
ll.append(5)
ll.append(6)
ll.show()