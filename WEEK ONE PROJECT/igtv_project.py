# Importing libraries i.e. pandas and xgboost

import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

# Load and prepare your dataset
try:
    data = pd.read_csv("MOCK_DATA (2).csv")

    # Check for missing values in the dataset
    if data.isnull().sum().sum() > 0:
        raise ValueError("Dataset contains missing values. Handle or remove them before proceeding.")

    # Separate features (X) and target variable (y)
    X = data.drop("videos", axis=1)
    y = data["videos"]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the XGBoost model
    model = xgb.XGBClassifier()
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model's accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"The accuracy of this model is: {accuracy:.2f}")

    # Generate a classification report for detailed metrics
    report = classification_report(y_test, y_pred)
    print("Classification Report:\n", report)

except FileNotFoundError:
    print("Error: The CSV file was not found. Please provide the correct file path.")
except ValueError as ve:
    print(f"Error: {str(ve)}")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
