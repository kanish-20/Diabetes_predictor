
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, confusion_matrix, classification_report
import joblib


df = pd.read_csv('diabetes.csv')


df.dropna(inplace=True)


X = df[[ 'Glucose', 'Insulin', 'BMI',  'Age']]
Y = df['outcome'] 


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


model = DecisionTreeClassifier()
model.fit(X_train, Y_train)


Y_pred = model.predict(X_test)



joblib.dump(model, 'decision_tree_diabetes_model.pkl')
print("✅ Model saved as decision_tree_diabetes_model.pkl")
