# 🧠 Telco Customer Churn Prediction App

Live App: [Churn Prediction Streamlit App](https://churn-prediction-app-3rdtimeacharm.streamlit.app/)  
Dataset Source: [Telco Customer Churn - Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)


## 🧪 ML Workflow

### 1. Data Preprocessing
- Removed missing values in `TotalCharges` column.
- Applied label encoding for binary categorical features.
- Used one-hot encoding for multi-class categorical variables.
- Scaled numerical features using `StandardScaler`.

### 2. Model Training
- Algorithms used:
  - ✅ Logistic Regression (as a baseline)
  - ✅ Random Forest Classifier (final model of choice)

### 3. Model Evaluation
- Metrics used:
  - Accuracy
  - F1 Score
  - ROC-AUC Score
- Final model showed strong performance on unseen test data.

### 4. Feature Importance (Explainability)
- Used the **feature importance** attribute of the Random Forest model to identify key drivers of churn.
- Top contributing features included:
  - `tenure`
  - `Contract`
  - `MonthlyCharges`
  - `PaymentMethod`
- Visualized feature importances using bar plots for stakeholder-friendly interpretation.


## 🧰 Tech Stack

| Tool | Purpose |
|------|---------|
| `Python` | Core development |
| `pandas`, `numpy` | Data manipulation |
| `scikit-learn` | Model building |
| `SHAP` | Model explainability |
| `matplotlib`, `seaborn` | EDA visualizations |
| `Streamlit` | App deployment |
| `GitHub` | Source control |
| `Kaggle` | Dataset source |


🤝 Collaboration & Feedback
Interested in collaborating? Found a bug? Want to reuse the pipeline?

📬 Reach out on [Linkedin](https://www.linkedin.com/in/oluwatosin-oyeladun-234a8a42/) or open an issue on this repo.
