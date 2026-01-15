# Import ColumnTransformer to apply different preprocessing to different columns
from sklearn.compose import ColumnTransformer

# Import encoders and scalers
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def build_preprocessor(num_cols, cat_cols):
    """
    Build preprocessing pipeline for numerical and categorical features.

    Parameters:
    num_cols (list): Numerical feature names
    cat_cols (list): Categorical feature names

    Returns:
    ColumnTransformer: Preprocessing object
    """

    # Create ColumnTransformer
    preprocessor = ColumnTransformer(
        transformers=[
            # Scale numerical columns
            ("num", StandardScaler(), num_cols),

            # One-hot encode categorical columns
            ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols)
        ]
    )

    # Return preprocessor
    return preprocessor
