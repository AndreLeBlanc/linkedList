class linked:
    def __init__(self, prev, nasta, data):
        self.data = data
        self.prev = prev
        self.nasta = nasta

    def setData(self, data):
        self.data = data

    def setPrev(self, prev):
        self.prev = prev

    def setNext(self, nasta):
        self.nasta = nasta

    def getPrev(self):
        return self.prev

    def getNext(self):
        return self.nasta

    def getData(self):
        return self.data
    

    
