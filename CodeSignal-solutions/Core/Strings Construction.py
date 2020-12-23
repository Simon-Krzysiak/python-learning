class Hist(dict):
    def count(self, x, count=1):
        self[x] = self.get(x,0) + count
        if self[x] == 0:
            del self[x]
            
    def contains(self, other):
        for key in other:
            if key not in self:
                return False
            elif other[key] > self[key]:
                return False
        return True
    
    def subtract(self, other):
        for key in other:
            self[key] -= other[key]
            if self[key] == 0:
                del self[key]
        

def stringsConstruction(a, b):
    needed = Hist()
    available = Hist()
    count = 0
    
    for char in a:
        needed.count(char,1)
    for char in b:
        available.count(char,1)
        
    while available.contains(needed):
        count += 1
        available.subtract(needed)
    
    return count
