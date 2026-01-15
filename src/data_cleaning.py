def clean_data(df):
    """
    Perform data cleaning operations:
    - Handle missing values
    - Normalize categorical text

    Parameters:
    df (pd.DataFrame): Raw dataset

    Returns:
    pd.DataFrame: Cleaned dataset
    """

    # Create a copy to avoid modifying original DataFrame
    df = df.copy()

    # Drop rows containing any missing values
    df.dropna(inplace=True)

    # Normalize brand names to lowercase for consistency
    df["Brand"] = df["Brand"].str.lower().str.strip()

    # Normalize fuel type values
    df["Fuel_Type"] = df["Fuel_Type"].str.lower().str.strip()

    # Normalize transmission values
    df["Transmission"] = df["Transmission"].str.lower().str.strip()

    # Normalize owner type values
    df["Owner_Type"] = df["Owner_Type"].str.lower().str.strip()

    # Normalize location values
    df["Location"] = df["Location"].str.lower().str.strip()

    # Return cleaned dataset
    return df
