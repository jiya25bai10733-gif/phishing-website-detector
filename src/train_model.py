import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

print("Loading dataset...")

data = pd.read_csv("../data/phishing.csv")


data = data.apply(pd.to_numeric, errors='coerce')
data = data.dropna()

X = data.iloc[:, :6]   
y = data.iloc[:, -1]

print("Using features:", X.columns)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

pickle.dump(model, open("../models/model.pkl", "wb"))
pickle.dump(list(X.columns), open("../models/features.pkl", "wb"))

print("✅ Model retrained with simple features!")