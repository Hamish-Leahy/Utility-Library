import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFE

def perform_rfe(X, y, n_features_to_select=5):
    """
    Perform Recursive Feature Elimination (RFE) with a RandomForestClassifier.

    Args:
        X (numpy.ndarray): Feature matrix.
        y (numpy.ndarray): Target labels.
        n_features_to_select (int, optional): Number of features to select. Defaults to 5.

    Returns:
        list: List of selected feature names.
    """
    model = RandomForestClassifier(random_state=42)
    rfe = RFE(model, n_features_to_select)
    rfe.fit(X, y)

    selected_features = [f for f, s in zip(X.columns, rfe.support_) if s]
    return selected_features

if __name__ == "__main__":
    # Load the Iris dataset
    data = load_iris()
    X, y = data.data, data.target
    feature_names = data.feature_names

    # Convert to a pandas DataFrame for convenience
    X = pd.DataFrame(X, columns=feature_names)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Perform Recursive Feature Elimination
    selected_features = perform_rfe(X_train, y_train, n_features_to_select=3)
    print("Selected Features:", selected_features)
