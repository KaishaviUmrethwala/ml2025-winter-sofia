import numpy as np
from sklearn.neighbors import KNeighborsRegressor

# Read N (number of data points)
N = int(input("Enter the number of data points (N): "))
if N <= 0:
    raise ValueError("N must be a positive integer.")

# Read k (number of neighbors)
k = int(input("Enter the number of neighbors (k): "))
if k <= 0:
    raise ValueError("k must be a positive integer.")

# Read N (x, y) points
X_data = []
y_data = []
print(f"Enter {N} data points (x, y):")
for i in range(N):
    x, y = map(float, input(f"Point {i+1} (x y): ").split())
    X_data.append(x)
    y_data.append(y)

# Convert lists to NumPy arrays
X_data = np.array(X_data).reshape(-1, 1)  # Reshape for sklearn
y_data = np.array(y_data)

# Calculate and print variance of labels
variance = np.var(y_data)
print(f"Variance of labels: {variance:.4f}")

# Read input X for prediction
X_pred = float(input("Enter X value for prediction: "))
X_pred = np.array([[X_pred]])  # Convert to 2D array

# Check if k is valid
if k > N:
    print("Error: k cannot be greater than N.")
else:
    # Create and train k-NN regressor
    knn = KNeighborsRegressor(n_neighbors=k)
    knn.fit(X_data, y_data)
    
    # Predict Y for input X
    y_pred = knn.predict(X_pred)
    print(f"Predicted Y value: {y_pred[0]:.4f}")