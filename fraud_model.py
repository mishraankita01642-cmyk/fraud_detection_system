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
amount = float(input("Enter amount: "))
location = int(input("Enter location (1=home,2=other,3=unknown): "))
foreign = int(input("Foreign transaction? (1=yes,0=no): "))
frequency = int(input("Transaction frequency: "))

import pandas as pd
new_transaction = pd.DataFrame([[amount, location, foreign, frequency]],columns=X.columns)
#predict
prediction = model.predict(new_transaction)
prob = model.predict_proba(new_transaction)

if prediction[0] == 1:
    print(" Fraud Detected")
else:
    print(" Safe Transaction")
    
print("Fraud Probability:", prob[0][1])
