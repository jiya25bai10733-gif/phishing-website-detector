import pickle
import pandas as pd
import matplotlib.pyplot as plt
import re
from feature_extraction import extract_features

print("Loading model...")

# ✅ Correct paths (no ../)
model = pickle.load(open("models/model.pkl", "rb"))
feature_names = pickle.load(open("models/features.pkl", "rb"))

print("Model loaded!")

# ⚠️ Warning message
print("⚠️ WARNING: This is an ML-based model still in training. Predictions may be inaccurate. Use for educational purposes only.\n")

url = input("Enter URL: ").lower()

phishing_score = 0

if "login" in url:
    phishing_score += 1
if "secure" in url:
    phishing_score += 1
if "verify" in url:
    phishing_score += 1
if "bank" in url:
    phishing_score += 1
if "update" in url:
    phishing_score += 1
if "free" in url:
    phishing_score += 1
if "paypal" in url:
    phishing_score += 1
if "@" in url:
    phishing_score += 1
if "-" in url:
    phishing_score += 1

# RULE-BASED CHECK
if phishing_score >= 2:
    print("\n--- Prediction Result ---")
    print("Safe Probability     : 10.00%")
    print("Phishing Probability : 90.00%")
    print("⚠️ Phishing Website (Rule-Based)")

    labels = ['Safe', 'Phishing']
    sizes = [10, 90]

# ML MODEL
else:
    features = extract_features(url, feature_names)
    features_df = pd.DataFrame([features], columns=feature_names)

    proba = model.predict_proba(features_df)[0]

    safe_prob = proba[0] * 100
    phishing_prob = proba[1] * 100

    print("\n--- Prediction Result ---")
    print(f"Safe Probability     : {safe_prob:.2f}%")
    print(f"Phishing Probability : {phishing_prob:.2f}%")

    if phishing_prob > safe_prob:
        print("⚠️ Phishing Website (ML)")
    else:
        print("✅ Legitimate Website")

    labels = ['Safe', 'Phishing']
    sizes = [safe_prob, phishing_prob]

# GRAPH
plt.figure()
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Website Safety Prediction")
plt.show()

