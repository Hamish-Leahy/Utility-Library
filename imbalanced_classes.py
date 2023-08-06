import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.utils import resample

def balance_classes(df, target_column, balance_method='over', random_state=None):
    """
    Balance the classes in the DataFrame using oversampling or undersampling.

    Args:
        df (pd.DataFrame): Input DataFrame.
        target_column (str): Name of the target column containing class labels.
        balance_method (str, optional): Method for balancing classes. 'over' for oversampling,
            'under' for undersampling. Defaults to 'over'.
        random_state (int, optional): Random seed for reproducibility. Defaults to None.

    Returns:
        pd.DataFrame: DataFrame with balanced classes.
    """
    # Count the occurrences of each class
    class_counts = df[target_column].value_counts()

    # Determine the class with the majority and minority samples
    majority_class = class_counts.idxmax()
    minority_class = class_counts.idxmin()

    # Get the number of samples in the minority class
    minority_count = class_counts[minority_class]

    if balance_method == 'over':
        # Oversample the minority class to match the majority class
        majority_df = df[df[target_column] == majority_class]
        minority_df = df[df[target_column] == minority_class]
        minority_upsampled = resample(minority_df, replace=True, n_samples=class_counts[majority_class], random_state=random_state)
        balanced_df = pd.concat([majority_df, minority_upsampled])
    elif balance_method == 'under':
        # Undersample the majority class to match the minority class
        majority_df = df[df[target_column] == majority_class]
        minority_df = df[df[target_column] == minority_class]
        majority_downsampled = resample(majority_df, replace=False, n_samples=class_counts[minority_class], random_state=random_state)
        balanced_df = pd.concat([minority_df, majority_downsampled])
    else:
        raise ValueError("Invalid balance_method. Use 'over' for oversampling or 'under' for undersampling.")

    return balanced_df

if __name__ == "__main__":
    # Sample DataFrame with imbalanced classes
    data = {'Class': ['A', 'B', 'A', 'B', 'A', 'A', 'A', 'B', 'B']}
    df = pd.DataFrame(data)

    # Balance the classes using oversampling
    df_balanced = balance_classes(df.copy(), target_column='Class', balance_method='over')
    print("Oversampled DataFrame:")
    print(df_balanced)

    # Balance the classes using undersampling
    df_balanced = balance_classes(df.copy(), target_column='Class', balance_method='under')
    print("\nUndersampled DataFrame:")
    print(df_balanced)
