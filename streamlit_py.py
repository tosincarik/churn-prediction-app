import streamlit as st

# Example user inputs
tenure = st.number_input("Tenure (months)", min_value=0, max_value=100, value=12)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, max_value=1000.0, value=50.0)
total_charges = st.number_input("Total Charges", min_value=0.0, max_value=10000.0, value=600.0)

contract_type = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
internet_type = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
tech_support = st.selectbox("Tech Support", ["Yes", "No"])
online_security = st.selectbox("Online Security", ["Yes", "No"])
payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])

# Your previously declared inputs
device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
multiple_lines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])

# Then build your input_data dictionary as before
input_data = {
    "tenure": tenure,
    "MonthlyCharges": monthly_charges,
    "TotalCharges": total_charges,
    "Contract_Month-to-month": int(contract_type == "Month-to-month"),
    "Contract_One year": int(contract_type == "One year"),
    "Contract_Two year": int(contract_type == "Two year"),
    "InternetService_DSL": int(internet_type == "DSL"),
    "InternetService_Fiber optic": int(internet_type == "Fiber optic"),
    "InternetService_No": int(internet_type == "No"),
    "TechSupport_No": int(tech_support == "No"),
    "OnlineSecurity_No": int(online_security == "No"),
    "PaymentMethod_Electronic check": int(payment_method == "Electronic check"),
    "DeviceProtection_No": int(device_protection == "No"),
    "DeviceProtection_No internet service": int(device_protection == "No internet service"),
    "DeviceProtection_Yes": int(device_protection == "Yes"),
    "MultipleLines_No": int(multiple_lines == "No"),
    "MultipleLines_No phone service": int(multiple_lines == "No phone service"),
    "MultipleLines_Yes": int(multiple_lines == "Yes"),
}
