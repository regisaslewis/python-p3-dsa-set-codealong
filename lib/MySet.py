class MySet:
    def __init__(self, enumerable = []):
        self.dictionary = {}
        for n in enumerable:
            self.dictionary[n] = True

    def has(self, value):
        return value in self.dictionary
    
    def add(self, value):
        self.dictionary[value] = True
        return self
    
    def delete(self, value):
        self.dictionary.pop(value, None)
        return self
    
    def size(self):
        return len(self.dictionary)
    
    def __str__(self):
        set = [str(n) for n in self.dictionary]
        return "MySet: {" + ",".join(set) + "}"
    
    def clear(self):
        for n in list(self.dictionary):
            self.dictionary.pop(n)
        return self.dictionary