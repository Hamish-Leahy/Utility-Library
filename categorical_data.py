import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

def label_encode_categorical(df, columns):
    """
    Label encode categorical columns in a DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame.
        columns (list): List of column names to label encode.

    Returns:
        pd.DataFrame: DataFrame with label encoded categorical columns.
    """
    label_encoder = LabelEncoder()
    for col in columns:
        df[col] = label_encoder.fit_transform(df[col])
    return df

def one_hot_encode_categorical(df, columns):
    """
    One-hot encode categorical columns in a DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame.
        columns (list): List of column names to one-hot encode.

    Returns:
        pd.DataFrame: DataFrame with one-hot encoded categorical columns.
    """
    df_encoded = pd.get_dummies(df, columns=columns, drop_first=True)
    return df_encoded

if __name__ == "__main__":
    # Sample DataFrame with categorical data
    data = {'Gender': ['Male', 'Female', 'Male', 'Female'],
            'City': ['New York', 'Chicago', 'Los Angeles', 'Chicago'],
            'Education': ['Bachelor', 'Master', 'PhD', 'Master']}
    df = pd.DataFrame(data)

    # Define the categorical columns to encode
    categorical_columns = ['Gender', 'City', 'Education']

    # Label encode the categorical columns
    df_label_encoded = label_encode_categorical(df.copy(), categorical_columns)
    print("Label Encoded DataFrame:")
    print(df_label_encoded)

    # One-hot encode the categorical columns
    df_one_hot_encoded = one_hot_encode_categorical(df.copy(), categorical_columns)
    print("\nOne-Hot Encoded DataFrame:")
    print(df_one_hot_encoded)
