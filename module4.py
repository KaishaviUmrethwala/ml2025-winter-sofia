# Ask for the number of inputs
N = int(input("Enter a positive integer N: "))

# Read N numbers into a list
numbers = []
for i in range(N):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Ask for X
X = int(input("Enter an integer X: "))

# Check if X exists in the list and print the result
if X in numbers:
    print(numbers.index(X) + 1)  # Output index (1-based)
else:
    print("-1")

# I tried following

# (venv) kumrethw@Kaishavis-MacBook-Pro ML % python3 module4.py
# Enter a positive integer N: 5
# Enter number 1: 3
# Enter number 2: 5
# Enter number 3: 7
# Enter number 4: 9
# Enter number 5: 10
# Enter an integer X: 5
# 2
# (venv) kumrethw@Kaishavis-MacBook-Pro ML % python3 module4.py
# Enter a positive integer N: 4
# Enter number 1: 2
# Enter number 2: 3
# Enter number 3: 4
# Enter number 4: 5
# Enter an integer X: 6
# -1