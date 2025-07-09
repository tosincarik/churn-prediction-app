input_data = {
    "tenure": tenure,
    "MonthlyCharges": monthly_charges,
    "TotalCharges": total_charges,

    # Contract type
    "Contract_Month-to-month": int(contract_type == "Month-to-month"),
    "Contract_One year": int(contract_type == "One year"),
    "Contract_Two year": int(contract_type == "Two year"),

    # Internet service
    "InternetService_DSL": int(internet_type == "DSL"),
    "InternetService_Fiber optic": int(internet_type == "Fiber optic"),
    "InternetService_No": int(internet_type == "No"),

    # Tech support and security
    "TechSupport_No": int(tech_support == "No"),
    "OnlineSecurity_No": int(online_security == "No"),

    # Payment method
    "PaymentMethod_Electronic check": int(payment_method == "Electronic check"),

    # DeviceProtection (new)
    "DeviceProtection_No": int(device_protection == "No"),
    "DeviceProtection_No internet service": int(device_protection == "No internet service"),
    "DeviceProtection_Yes": int(device_protection == "Yes"),

    # MultipleLines (new)
    "MultipleLines_No": int(multiple_lines == "No"),
    "MultipleLines_No phone service": int(multiple_lines == "No phone service"),
    "MultipleLines_Yes": int(multiple_lines == "Yes"),
}  # <-- Make sure this closing brace is present
