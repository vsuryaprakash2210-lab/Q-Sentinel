import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from sklearn.metrics import roc_auc_score, accuracy_score

# -----------------------------
# 1. Load data (NO labels)
# -----------------------------
train_df = pd.read_csv("train.csv")
test_df  = pd.read_csv("test.csv")

X_train = train_df.values
X_test  = test_df.values

# -----------------------------
# 2. Hidden truth (only for evaluation)
# First 1200 = normal, Last 200 = scammer
# NOT used for training
# -----------------------------
y_test = np.array([0]*1200 + [1]*200)

# -----------------------------
# 3. Feature scaling
# -----------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

# -----------------------------
# 4. Classical Anomaly Detector
# (Learns what "normal user" looks like)
# -----------------------------
iso_model = IsolationForest(
    n_estimators=200,
    contamination=0.15,
    random_state=42
)

iso_model.fit(X_train_scaled)

# Decision scores (higher = more normal)
scores = iso_model.decision_function(X_test_scaled)

# Convert to 0–1 risk
classical_risk = 1 - (
    (scores - scores.min()) /
    (scores.max() - scores.min())
)

# -----------------------------
# 5. Quantum Risk Amplifier
# (Quantum-inspired state amplification)
# -----------------------------
# This represents how quantum probability
# amplifies subtle deviations
quantum_risk = np.sqrt(classical_risk)

# -----------------------------
# 6. Hybrid Ensemble Fusion
# -----------------------------
final_risk = 0.6 * classical_risk + 0.4 * quantum_risk

# Scale to 0–100 for real-world use
final_risk_score = final_risk * 100

# -----------------------------
# 7. Fraud decision threshold
# -----------------------------
threshold = 60
predicted = (final_risk > 0.60).astype(int)

# -----------------------------
# 8. Evaluation
# -----------------------------
roc_auc = roc_auc_score(y_test, final_risk)
accuracy = accuracy_score(y_test, predicted)

print("\nMODEL PERFORMANCE")
print("-----------------------------")
print("ROC–AUC :", round(roc_auc, 4))
print("Accuracy:", round(accuracy * 100, 2), "%")

# -----------------------------
# 9. Output Risk Table
# -----------------------------
results = pd.DataFrame({
    "Classical_Risk": classical_risk,
    "Quantum_Risk": quantum_risk,
    "Final_Risk_Score": final_risk_score
})

results["Flagged"] = results["Final_Risk_Score"] > 60

results.to_csv("risk_output.csv", index=False)

print("\nTop High-Risk Sessions:")
print(results.sort_values("Final_Risk_Score", ascending=False).head(10))
