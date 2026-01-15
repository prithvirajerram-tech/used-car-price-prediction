# Import pandas for reading CSV files
import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """
    Load dataset from a CSV file.

    Parameters:
    path (str): Path to the CSV file

    Returns:
    pd.DataFrame: Loaded dataset
    """
    # Read CSV file into a DataFrame
    df = pd.read_csv(r"C:\Users\prith\Desktop\BlockStripe\MLPipilineProject\used_cars_data.csv")

    # Return the loaded DataFrame
    return df
