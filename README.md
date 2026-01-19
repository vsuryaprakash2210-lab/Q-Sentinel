# 🛡️ Q-Sentinel  
### Quantum-Enhanced Behavioral Risk Detection System

Q-Sentinel is a hybrid **quantum–classical AI system** designed to detect **high-risk behavioral anomalies** in user activity data by learning only normal user behavior and assigning a continuous risk score.

> ⚠️ This project is designed for **research, experimentation, and decision-support purposes only**. It does not replace production-grade or regulated fraud detection systems.

---

## 🎯 Problem Statement

Traditional fraud detection systems struggle due to:
- Lack of reliable scammer labels
- Rapidly evolving fraud patterns
- High false positives from rule-based systems
- Late detection after financial loss
- Poor explainability and auditability

Q-Sentinel addresses these challenges using **unsupervised learning combined with quantum-inspired risk amplification** to identify suspicious behavior early.

---

## ✨ Key Features

- 🧠 **Unsupervised Learning (No Fraud Labels Required)**  
  Trains only on normal user behavior data.

- 📊 **Continuous Risk Scoring (0–100)**  
  Outputs interpretable risk scores instead of binary predictions.

- 🌲 **Classical Anomaly Detection**  
  Uses Isolation Forest to learn normal behavioral boundaries.

- ⚛️ **Quantum-Inspired Risk Modeling**  
  Amplifies anomaly signals using quantum probability principles.

- 🔗 **Hybrid Ensemble Architecture**  
  Combines classical and quantum risk scores into a single final score.

- 📈 **Scammer Detection Accuracy Evaluation**  
  Measures how effectively high-risk scores capture scammer behavior.

---

## 🧠 How It Works (High-Level)

1. User session data is collected  
2. Features are scaled and normalized  
3. Classical model learns normal behavior  
4. Anomaly scores are generated  
5. Scores are mapped into quantum-inspired states  
6. Quantum probabilities amplify subtle risks  
7. Classical and quantum risks are combined  
8. Final risk score is produced  

---

## 🧩 Data Description

Each row represents a **user session** with behavioral metrics such as:
- Session duration
- Time gaps between actions
- Transaction frequency
- Activity distribution patterns

### Training Data
- Contains **only normal user behavior**
- No labels (`0` or `1`)

### Test Data
- Contains both normal and scammer-like behavior
- Labels are used **only for evaluation**, not training

---

## 📊 Risk Interpretation

| Risk Score | Meaning        | Action Suggestion       |
|-----------|---------------|-------------------------|
| 0–40      | Normal        | No action               |
| 40–60     | Mild anomaly  | Monitor                 |
| 60–75     | Suspicious    | Manual review           |
| 75–100    | High risk     | Block / investigate     |

---

## 📈 Accuracy & Evaluation

Although the model is **trained in an unsupervised manner**:

- Training data contains **only synthetic normal user behavior**
- Test data includes **synthetic scammer behavior** (used only for evaluation)

### Accuracy is computed based on:
- Whether scammer samples receive **high risk scores**
- Threshold-based classification on the final risk score

### Example Metrics

```text
Accuracy : 97%
ROC-AUC  : 1.00
```

---
## 🧩 Technology Stack

- Python 3.9+
- NumPy
- Pandas
- Scikit-learn
- Quantum-inspired probability modeling
- Hybrid ensemble architecture

---

## ⚙️ Installation

### Prerequisites
- Python 3.9 or higher
- pip

---

### The system will:

- Train on synthetic normal user data
- Score all test sessions
- Output final risk scores
- Compute accuracy based on scammer detection

---

## 📝 Logging & Outputs

### The system provides:
- Risk scores for each test session
- Classical and quantum risk components
- Accuracy and ROC metrics

### Useful for:
- Research analysis
- Model tuning
- Explainability and audits

---

## ✅ Advantages

- ✔ No real user data required
- ✔ No scammer labels needed for training
- ✔ Detects unknown fraud patterns
- ✔ Continuous, explainable risk output
- ✔ Hybrid quantum–classical design
- ✔ Future-ready for quantum integration

---

## ⚠️ Limitations

- ❌ Uses simulated quantum logic
- ❌ Threshold selection affects accuracy
- ❌ Requires retraining for behavior drift
- ❌ Not production-ready for financial systems

---

## 🔮 Future Enhancements

- Integration with real quantum backends
- Temporal sequence modeling
- Real-time API deployment
- Risk dashboard visualization
- Adaptive user-specific thresholds
- Regulatory explainability modules
