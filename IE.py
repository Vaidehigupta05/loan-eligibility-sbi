import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Config
st.set_page_config(page_title="SBI Loan Eligibility Checker", page_icon="🏦", layout="wide")

# Custom Styling
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
        }
        .stButton>button {
            background-color: #1f77b4;
            color: white;
            font-size: 16px;
            border-radius: 8px;
        }
        .stSidebar {
            background-color: #e6f0ff;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("🏦 Loan Eligibility Checker – SBI")
st.markdown("### Smart, Fast & Reliable Loan Eligibility Assessment")

# Layout: 2 Columns
col1, col2 = st.columns([1, 2])

# Sidebar Inputs
st.sidebar.header("Enter Your Details")

age = st.sidebar.number_input("Age", min_value=18, max_value=65, value=25)
income = st.sidebar.number_input("Monthly Income (₹)", min_value=0, value=30000)
loan_amount = st.sidebar.number_input("Requested Loan Amount (₹)", min_value=0, value=500000)
credit_score = st.sidebar.slider("Credit Score", 300, 900, 700)
employment = st.sidebar.selectbox("Employment Type", ["Salaried", "Self-Employed"])

# Eligibility Logic
def check_eligibility(age, income, loan_amount, credit_score, employment):
    
    if age < 21:
        return "Not Eligible", "Minimum age is 21"
    
    if credit_score < 650:
        return "Not Eligible", "Low credit score"
    
    if income < 25000:
        return "Not Eligible", "Income too low"
    
    if loan_amount > income * 20:
        return "Not Eligible", "Loan too high"
    
    if employment == "Self-Employed" and income < 30000:
        return "Not Eligible", "Higher income required"
    
    return "Eligible", "You meet all criteria"

# Button Action
if st.sidebar.button("Check Eligibility"):
    status, message = check_eligibility(age, income, loan_amount, credit_score, employment)

    with col1:
        st.subheader("Result")
        if status == "Eligible":
            st.success(f"✅ {status}\n\n{message}")
        else:
            st.error(f"❌ {status}\n\n{message}")

    # Graph Section
    with col2:
        st.subheader("📊 Loan vs Eligibility Analysis")

        max_loan_allowed = income * 20

        data = pd.DataFrame({
            "Category": ["Your Loan", "Max Eligible Loan"],
            "Amount": [loan_amount, max_loan_allowed]
        })

        fig, ax = plt.subplots()
        ax.bar(data["Category"], data["Amount"])
        ax.set_ylabel("Amount (₹)")
        ax.set_title("Loan Comparison")

        st.pyplot(fig)

# Info Section
st.markdown("---")
st.header("📌 Eligibility Criteria")

st.info("""
✔ Minimum Age: 21 years  
✔ Minimum Income: ₹25,000/month  
✔ Minimum Credit Score: 650  
✔ Loan Amount ≤ 20 × Monthly Income  
""")

# Footer
st.markdown("---")
st.caption("Developed as a prototype for SBI Loan Eligibility System")