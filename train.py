# Import custom modules
from src.data_loading import load_data
from src.data_cleaning import clean_data
from src.feature_engineering import add_features
from src.preprocessing import build_preprocessor
from src.model_training import train_model

# Load dataset from CSV
df = load_data("data/used_cars.csv")

# Clean raw dataset
df = clean_data(df)

# Add engineered features
df = add_features(df)

# Separate features and target variable
#X = df.drop("Price", "New_Price", axis=1)
X = df.drop(columns=["Price", "New_Price"])
y = df["Price"]

# Identify numerical columns
num_cols = X.select_dtypes(exclude="object").columns

# Identify categorical columns
cat_cols = X.select_dtypes(include="object").columns

# Build preprocessing pipeline
preprocessor = build_preprocessor(num_cols, cat_cols)

print("Training columns:")
print(X.columns.tolist())

# Train the model pipeline
model = train_model(preprocessor, X, y)

print("Model training completed successfully!")

import pickle

# Save trained pipeline to disk
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved as model.pkl")
