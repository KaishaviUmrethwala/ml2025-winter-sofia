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

def main():
    processor = NumberProcessor()

    while True:
        try:
            N = int(input("Enter a positive integer (N): "))
            if N > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    print(f"Enter {N} numbers:")
    for _ in range(N):
        while True:
            try:
                num = int(input())
                processor.insert_number(num)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    while True:
        try:
            X = int(input("Enter a number to search (X): "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    print(processor.search_number(X))

if __name__ == "__main__":
    main()
