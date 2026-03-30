# 🔐 Phishing Website Detector

## 📌 Project Description
This project is an AI/ML-based system that detects whether a given URL is **phishing or legitimate**.

Phishing websites are fake websites designed to steal sensitive information such as passwords, banking details, and personal data. This project uses both **Machine Learning** and **rule-based techniques** to improve detection accuracy.

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/jiya25bai10733-gif/phishing-website-detector.git
cd phishing-website-detector
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
---
## How to Run (Single Command)
```bash
python run.py
```
---
## 🧠 How It Works
- User enters a URL
- Rule-based checks are applied
- If suspicious → flagged as phishing
- Otherwise → Machine Learning model predicts probabilities
- Output is displayed along with a graph
---
## Features used
- URL length
- Number of dots in URL
- Presence of HTTPS
- Special characters (@, -)
- Suspicious keywords (login, secure, verify, bank, update, free, paypal)
- Domain-based features

  ---
  
  ## 🖥️ Application Features
- Simple CLI-based interface
- Real-time URL prediction
- Combination of rule-based + ML detection
- Graphical output using pie chart
  
  ---
  
## Model Performance
- Accuracy: ~80–90%
- Model used: Logistic Regression / Random Forest
  
  ---
  
  ## Future Improvements
- Improve accuracy using advanced models (XGBoost, Deep Learning)
- Build a web interface
- Add real-time browser extension

  ---

  ## Note
- This project is developed as part of the Fundamentals of AI & ML BYOP Course Project.
- The model is still under training and may not always give accurate results.
- Integrate phishing blacklist APIs
