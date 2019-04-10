class TNode(object):
    def __init__(self, data):
        self.left = None #Left subtree
        self.right = None #Right subtree
        self.data = data #Data member
    def Print(self):
        print(self.data)


class BST:
    def __init__(self):
        self.root = None



    def preorder(self,node): # metoda pro prochazeni a tisknuti stromu
        if node == None: # pokud nema nasledovnika
            return
        print(node.data)
        if node.left != None: # pokud existuje levy, rekurzivne volame metodu
            self.preorder(node.left)
        if node.right != None:
            self.preorder(node.right)

    def preorder_stack(self): # metoda pro prochazeni stromu se zasobnikem
        if self.root == None: #pokud neexistuje koren
            return
        else:
            S = []
            S.append(self.root) #jinak pridame koren
            while S: # dokud jsou v zasobniku prvky
                node = S.pop()  # odebereme posledni prvek
                print(node.data)
                if node.right != None:
                    S.append(node.right) # pridame pravy
                if node.left != None:
                    S.append(node.left) # pridame levy

    def add(self,data): # metoda pridani prvku do stromu
        if self.root is None: # # pokud nema koren, vytvorim
            self.root = TNode(data)
        else:
            node = self.root
            p = None # predchudce
            while node: # pokud existuje nasledovnik
                p = node
                if data < node.data: # pokud je prvek mensi jak uzel, pridame doleva
                    node = node.left
                elif data > node.data:
                    node = node.right
                else:
                    return None

            if data < p.data:
                p.left = TNode(data) # pokud je prvek mensi jako posledni nenulovy, vytvorim novy uzel
            else:
                p.right = TNode(data)

    def find(self,data):
        s = "0"
        if self.root is None:
            return None, None
        else:
            node = self.root
            p = None  # predchudce
            while node:  # pokud existuje nasledovnik
                print("N: {}, L: {}, R: {}".format(node.data,node.left,node.right))
                if data < node.data:  # pokud je prvek mensi jak uzel, pridame doleva
                    p = node
                    node = node.left
                    s = s + '0'
                elif data > node.data:
                    p = node
                    node = node.right
                    s = s + '1'
                else:
                    return node, p
            return p, None

    def delete(self,data):
        cur,pred = self.find(data)
        print("ND: {}, L: {}, R: {}".format(cur.data,cur.left,cur.right))
        if (cur.left is None) and (cur.right is None):
            print("Deleting leaf")
            self.delLeaf(cur,pred)
        elif cur.left is not None and cur.right is not None:
            print("Deleting TwoSt")
            self.delTwoSt(cur,pred)
        else:
            print("Deleting OneSt, cur: {}, pred: {}".format(cur.data,pred.data))
            self.delOneSt(cur,pred)


    def delLeaf(self, cur, pred):
        if pred == None:
            self.root = None
        elif pred.left == cur:
            pred.left = None
        else:
            pred.right = None

    def delOneSt(self,cur,pred): # mám jednoho syna
        # cur je kořen
        if pred is None:
            self.root = cur.left if cur.left is not None else cur.right
            return

        # cur je levý syn
        if pred.left == cur:
            if cur.left is not None:
                pred.left = cur.left
            else:
                pred.left = cur.right
        # cur je pravý syn
        else:
            if cur.left is not None:
                pred.right = cur.left
            else:
                pred.right = cur.right

    def findNext(self,cur):
        if cur.right is None:
            return None,None

        # udělám krok doprava
        pred = cur
        node = cur.right
        # jdu doleva, dokud můžu
        while node.left is not None:
            pred = node
            node = node.left
        # vrátím (cur, pred)
        return node,pred


    def delTwoSt(self,cur,pred): # mám oba syny
        (anext, anextpred) = self.findNext(cur)
        # zapamatuji hodnotu anextu
        val = anext.data
        # smažu anext
        self.delete(anext.data)
        # v cur nahradím hodnotu
        cur.data = val





bst = BST()
bst.add(10)
bst.add(12)
bst.add(11)
bst.add(9)
bst.add(1)
bst.add(90)
bst.preorder_stack()
#p, node = bst.find(14)
bst.delete(9)
bst.delete(10)
print("====")
bst.preorder_stack()

#p.Print()
#node.Print()

