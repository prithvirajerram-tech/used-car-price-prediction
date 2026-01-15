# Import evaluation metrics
from sklearn.metrics import r2_score, mean_absolute_error

def evaluate(model, X_test, y_test):
    """
    Evaluate model performance.

    Parameters:
    model (Pipeline): Trained model pipeline
    X_test (pd.DataFrame): Test features
    y_test (pd.Series): True target values

    Returns:
    dict: Evaluation metrics
    """

    # Generate predictions
    predictions = model.predict(X_test)

    # Calculate R² score
    r2 = r2_score(y_test, predictions)

    # Calculate Mean Absolute Error
    mae = mean_absolute_error(y_test, predictions)

    # Return metrics as dictionary
    return {
        "r2": r2,
        "mae": mae
    }
