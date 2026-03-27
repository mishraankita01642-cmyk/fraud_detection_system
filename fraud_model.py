import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load data
data = pd.read_csv("data.csv")

# Features and labels
X = data.drop("fraud", axis=1)
y = data["fraud"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Test accuracy
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)

# Predict new transaction
new_transaction = [[6000, 2, 1, 12]]  # Example input
prediction = model.predict(new_transaction)

if prediction[0] == 1:
    print(" Fraud Detected")
else:
    print(" Safe Transaction")