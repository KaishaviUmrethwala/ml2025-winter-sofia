import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    # Read the number of points
    N = int(input("Enter the number of (x, y) points: "))
    
    # Initialize an array to store (x, y) values
    data = np.zeros((N, 2), dtype=int)
    
    # Read the (x, y) pairs
    for i in range(N):
        x, y = map(int, input(f"Enter x and y for point {i+1}: ").split())
        data[i] = [x, y]
    
    # Extract X (ground truth) and Y (predictions)
    X = data[:, 0]
    Y = data[:, 1]
    
    # Compute precision and recall
    precision = precision_score(X, Y, zero_division=0)
    recall = recall_score(X, Y, zero_division=0)
    
    # Print results
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")

if __name__ == "__main__":
    main()