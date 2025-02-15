class NumberProcessor:
    def __init__(self):
        
        self.numbers = []

    def insert_number(self, number):
        
        self.numbers.append(number)

    def search_number(self, target):
        
        try:
            return self.numbers.index(target) + 1  
        except ValueError:
            return -1
