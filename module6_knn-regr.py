import numpy as np

def euclidean_distance(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))

def knn_regression(points, values, X, k):
    distances = np.array([euclidean_distance(np.array([x]), np.array([X])) for x in points])
    sorted_indices = np.argsort(distances)
    nearest_neighbors = values[sorted_indices[:k]]
    return np.mean(nearest_neighbors)

def main():
    try:
        N = int(input("Enter the number of data points (N): "))
        if N <= 0:
            raise ValueError("N must be a positive integer.")

        k = int(input("Enter the number of neighbors (k): "))
        if k <= 0:
            raise ValueError("k must be a positive integer.")
        if k > N:
            raise ValueError("k cannot be greater than N.")

        points = np.zeros(N)
        values = np.zeros(N)

        for i in range(N):
            x, y = map(float, input(f"Enter point {i+1} (x y): ").split())
            points[i] = x
            values[i] = y

        X = float(input("Enter the query point X: "))
        Y_pred = knn_regression(points, values, X, k)
        print(f"Predicted Y value: {Y_pred:.4f}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
