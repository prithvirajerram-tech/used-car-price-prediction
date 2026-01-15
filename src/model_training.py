# Import XGBoost regressor
from xgboost import XGBRegressor

# Import Pipeline to chain preprocessing and model
from sklearn.pipeline import Pipeline

def train_model(preprocessor, X_train, y_train):
    """
    Train XGBoost regression model inside a pipeline.

    Parameters:
    preprocessor (ColumnTransformer): Feature preprocessor
    X_train (pd.DataFrame): Training features
    y_train (pd.Series): Target variable

    Returns:
    Pipeline: Trained ML pipeline
    """

    # Initialize XGBoost regressor with tuned parameters
    model = XGBRegressor(
        n_estimators=300,
        max_depth=6,
        learning_rate=0.05,
        random_state=42
    )

    # Combine preprocessing and model into a single pipeline
    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model)
        ]
    )

    # Train pipeline on training data
    pipeline.fit(X_train, y_train)

    # Return trained pipeline
    return pipeline
