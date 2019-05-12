import linked

class Listan:
    def __init__(self):
        self.first = "null"
        self.last = "null"
        self.len = 0

    def langd(self):
        return self.len

    def forst(self):
        if self.first != "null":
            return self.first.getData()

    def sist(self):
        if self.last != "null":
            return self.last.getData()

    def laggTill(self, data):
        curr = self.last
        new = linked.linked(curr, "null", data)
        if curr != "null":
            curr.setNext(new)
        if self.first == "null":
            self.first = new
        self.last = new
        self.len += 1


    def laggInForst(self, data):
        new = linked.linked("null", self.first, data)
        if self.first != "null":
            self.first.setPrev(new)
            self.first = new
        else:
            self.last = new
            self.first = new
        self.len += 1

    def mitten(self, index, data):
        i = 0
        curr = self.first
        while (i != index) and (i < self.len):
            curr = curr.getNext()
            i += 1
        new = linked.linked(curr.getPrev(), curr, data)
        curr.getPrev().setNext(new)
        curr.setPrev(new)
        self.len += 1

    def sattIn(self, data, index):
        if index == 0:
            self.laggInForst(data)
            
        elif (0 < index) and (index < self.len):
            self.mitten(index, data)

        elif index == self.len:
            self.laggTill(data)

    def fetch(self, index):
        if (0 <= index) and (index < self.len):
            cur = self.first
            for i in range(0, index):
                cur = cur.getNext()
            return cur.getData()
        
    def rem(self, index):
        if (0 <= index) and (index < self.len-1):
            curr = self.first
            if 0 < index: 
                for _ in range(0, index):
                    curr = curr.getNext()
                curr.getPrev().setNext(curr.getNext())
                curr.getNext().setPrev(curr.getPrev())
            elif index == 0:
                curr.getNext().setPrev("null")
                self.first = curr.getNext()
                curr.setNext("null")
            self.len -= 1
        elif index == self.len-1:
            self.remLast()
            
    def remLast(self):
        if self.last != "null":
            oldLast = self.last
            if oldLast.getPrev() != "null":
                newLast = oldLast.getPrev()
                newLast.setNext("null")
                self.last = newLast
            else:
                self.first  = "null"
                self.last = "null"
            self.len -= 1
            
    def all(self):
        cur = self.first
        while cur != "null":
            print(cur.getData())
            cur = cur.getNext()
           
