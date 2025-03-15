import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

def get_data_set(size):
    X = np.empty(size)
    y = np.empty(size, dtype=int)
    for i in range(size):
        X[i] = float(input("Enter x value: "))
        y[i] = int(input("Enter y value: "))
    return X.reshape(-1, 1), y

def main():
    # Get Training Data
    N = int(input("Enter number of training samples (N): "))
    X_train, y_train = get_data_set(N)
    
    # Get Test Data
    M = int(input("Enter number of test samples (M): "))
    X_test, y_test = get_data_set(M)
    
    # Define k values to search
    param_grid = {'n_neighbors': list(range(1, 11))}
    
    # Perform GridSearchCV
    knn = KNeighborsClassifier()
    grid_search = GridSearchCV(knn, param_grid, cv=5, scoring='accuracy')
    grid_search.fit(X_train, y_train)
    
    # Get Best k
    best_k = grid_search.best_params_['n_neighbors']
    
    # Evaluate on test data
    best_knn = KNeighborsClassifier(n_neighbors=best_k)
    best_knn.fit(X_train, y_train)
    y_pred = best_knn.predict(X_test)
    test_accuracy = accuracy_score(y_test, y_pred)
    
    print(f"Best k: {best_k}")
    print(f"Test Accuracy: {test_accuracy:.4f}")

if __name__ == "__main__":
    main()
