from module5_mod import NumberProcessor

def main():
    processor = NumberProcessor()

    # Get the count of numbers
    while True:
        try:
            N = int(input("Enter a positive integer (N): "))
            if N > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    # Get N numbers from the user
    print(f"Enter {N} numbers:")
    for _ in range(N):
        while True:
            try:
                num = int(input())
                processor.insert_number(num)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    # Get the number to search for
    while True:
        try:
            X = int(input("Enter a number to search (X): "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Search and print the result
    result = processor.search_number(X)
    print(result)

if __name__ == "__main__":
    main()
