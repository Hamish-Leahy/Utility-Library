import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

def evaluate_classification_model(y_true, y_pred, target_names=None):
    """
    Evaluate a classification model using common metrics.

    Args:
        y_true (numpy.ndarray or list): True labels.
        y_pred (numpy.ndarray or list): Predicted labels.
        target_names (list, optional): Names of target classes. Defaults to None.

    Returns:
        dict: Dictionary containing the evaluation metrics.
    """
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average='weighted')
    recall = recall_score(y_true, y_pred, average='weighted')
    f1 = f1_score(y_true, y_pred, average='weighted')
    cm = confusion_matrix(y_true, y_pred)

    evaluation_metrics = {
        'Accuracy': accuracy,
        'Precision': precision,
        'Recall': recall,
        'F1 Score': f1,
        'Confusion Matrix': cm
    }

    if target_names:
        evaluation_metrics['Classification Report'] = pd.DataFrame(classification_report(y_true, y_pred, target_names=target_names, output_dict=True))

    return evaluation_metrics

if __name__ == "__main__":
    # Sample true and predicted labels for a binary classification problem
    y_true = [1, 0, 1, 0, 1]
    y_pred = [1, 1, 0, 0, 1]

    # Evaluate the classification model
    evaluation_results = evaluate_classification_model(y_true, y_pred)
    for metric, value in evaluation_results.items():
        print(f"{metric}: {value}")
