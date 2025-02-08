from collections import defaultdict
from sortedcontainers import SortedSet

class NumberContainers:
    def __init__(self):
        self.numberToIndices = defaultdict(SortedSet)
        self.indexToNumber = {}
        
        
    def change(self, index: int, number: int) -> None:
        if index in self.indexToNumber:
            originalNumber = self.indexToNumber[index]
            self.numberToIndices[originalNumber].remove(index)
            if len(self.numberToIndices[originalNumber]) == 0:
               del self.numberToIndices[originalNumber]
        self.indexToNumber[index] = number
        self.numberToIndices[number].add(index)
            
    def find(self, number: int) -> int:
        if number in self.numberToIndices:
            return self.numberToIndices[number][0]
        return -1
    
    
if __name__ == "__main__":
    nc = NumberContainers()
    print(nc.find(10)) # There is no index that is filled with number 10. Therefore, we return -1.
    nc.change(2, 10) # Your container at index 2 will be filled with number 10.
    nc.change(1, 10) # Your container at index 1 will be filled with number 10.
    nc.change(3, 10) # Your container at index 3 will be filled with number 10.
    nc.change(5, 10) # Your container at index 5 will be filled with number 10.
    print(nc.find(10)) # Number 10 is at the indices 1, 2, 3, and 5. Since the smallest index that is filled with 10 is 1, we return 1.
    nc.change(1, 20) # Your container at index 1 will be filled with number 20. Note that index 1 was filled with 10 and then replaced with 20. 
    print(nc.find(10)) # Number 10 is at the indices 2, 3, and 5. The smallest index that is filled with 10 is 2. Therefore, we return 2.