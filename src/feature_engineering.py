def add_features(df):
    """
    Create new features from existing columns.

    Parameters:
    df (pd.DataFrame): Cleaned dataset

    Returns:
    pd.DataFrame: Dataset with engineered features
    """

    # Copy DataFrame to avoid side effects
    df = df.copy()

    # Calculate car age from manufacturing year
    df["car_age"] = 2024 - df["Year"]

    # Return updated DataFrame
    return df
