# Fraud Detection System using Machine Learning

## Project Overview
This project is a **Fraud Detection System** built using Python and Machine Learning.  
It predicts whether a transaction is **fraudulent or legitimate** based on user input.

The system uses a trained machine learning model to analyze transaction patterns and provide predictions along with probability scores.


##  Features
- Predicts fraud in real-time
- Uses Machine Learning (Random Forest)
- Takes user input from terminal
- Provides probability of fraud
- Simple and easy to use

## Technologies Used
- Python
- Scikit-learn
- Pandas

##  Project Structure

fraud_detection_system/ │ ├── fraud_model.py       # Main Python file ├── data.csv             # Dataset └── README.md            # Project documentation

##  Installation & Setup

1.Clone the repository

git clone https://github.com/your-username/fraud-detection-system.git
cd fraud-detection-system

2.Install required libraries

pip install pandas scikit-learn

3.How to Run the Project

Run the Python file:
python fraud_model.py

4.Input Details

You will be asked to enter:
Input	Description
Amount	Transaction amount
Location	1 = Home, 2 = Other, 3 = Unknown
Foreign	0 = No, 1 = Yes
Frequency	Number of transactions

Output
The system will display:
Safe Transaction
Fraud Detected
Fraud Probability (e.g., 0.87)

## How It Works
1. Dataset is loaded using Pandas
2. Data is split into training and testing sets
3. Model is trained using Random Forest
4. User input is taken from terminal
5. Input is converted into structured format
6. Model predicts fraud or safe transaction


## Challenges Faced
Handling input in terminal
File path issues
Data format warnings
Understanding ML concepts

## Future Improvements
Use real-world datasets
Improve model accuracy
Add GUI or web interface
Deploy the system online


## Author

Ankita
B.Tech CSE Core


## Conclusion

This project demonstrates how machine learning can be used to detect fraudulent transactions efficiently. It highlights the importance of AI in solving real-world financial problems.

