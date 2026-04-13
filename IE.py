import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Config
st.set_page_config(page_title="SBI Loan Dashboard", layout="wide")

# Custom CSS (Dark Theme)
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
h1, h2, h3, h4 {
    color: #ffffff;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align:center; color:#00a2ff;'>STATE BANK OF INDIA</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>🏦 Smart Loan Eligibility Dashboard</h3>", unsafe_allow_html=True)

st.markdown("---")

# KPI Section
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Applications Today", "1,245", "+5%")

with col2:
    st.metric("Approved Loans", "320", "+2%")

with col3:
    st.metric("Rejected Loans", "85", "-1%")

st.markdown("---")

# Input Section
st.subheader("🔍 Check Loan Eligibility")

col1, col2 = st.columns(2)

with col1:
    income = st.number_input("Monthly Income (₹)", value=30000)
    loan_amount = st.number_input("Loan Amount (₹)", value=500000)

with col2:
    credit_score = st.slider("Credit Score", 300, 900, 700)
    age = st.slider("Age", 18, 65, 25)

# -------------------------------
# LOGIC FUNCTIONS
# -------------------------------

def check_eligibility(income, loan_amount, credit_score, age):
    if age < 21:
        return "Not Eligible", "Minimum age is 21"
    if credit_score < 650:
        return "Not Eligible", "Low credit score"
    if income < 25000:
        return "Not Eligible", "Income too low"
    if loan_amount > income * 20:
        return "Not Eligible", "Loan too high"
    return "Eligible", "You meet all criteria"

def calculate_score(income, loan_amount, credit_score, age):
    score = 0
    
    if credit_score > 750:
        score += 40
    elif credit_score > 650:
        score += 30

    if income > 50000:
        score += 30
    elif income > 25000:
        score += 20

    if loan_amount < income * 15:
        score += 20

    if age >= 25:
        score += 10

    return score

def give_suggestions(income, loan_amount, credit_score):
    suggestions = []

    if credit_score < 650:
        suggestions.append("Improve credit score above 650")

    if income < 25000:
        suggestions.append("Increase income or add co-applicant")

    if loan_amount > income * 20:
        suggestions.append(f"Reduce loan amount below ₹{income*20}")

    return suggestions

# -------------------------------
# BUTTON ACTION
# -------------------------------

if st.button("Check Eligibility"):

    status, message = check_eligibility(income, loan_amount, credit_score, age)
    score = calculate_score(income, loan_amount, credit_score, age)
    suggestions = give_suggestions(income, loan_amount, credit_score)

    # Result
    st.markdown("## 🧾 Result")
    if status == "Eligible":
        st.success(f"✅ {status} — {message}")
    else:
        st.error(f"❌ {status} — {message}")

    # Score
    st.markdown("## 📊 Eligibility Score")
    st.progress(score / 100)
    st.write(f"Score: {score}/100")

    # Suggestions
    if suggestions:
        st.markdown("## 💡 Suggestions to Improve")
        for s in suggestions:
            st.write("- " + s)

    st.markdown("---")

    # Graph Section
    st.markdown("## 📈 Loan Affordability Analysis")

    safe_loan = income * 20
    risk_loan = income * 25

    data = pd.DataFrame({
        "Category": ["Safe Limit", "Risk Limit", "Your Loan"],
        "Amount": [safe_loan, risk_loan, loan_amount]
    })

    fig, ax = plt.subplots()
    ax.bar(data["Category"], data["Amount"])
    ax.set_ylabel("Amount (₹)")
    ax.set_title("Loan Comparison")

    st.pyplot(fig)

# Footer
st.markdown("---")
st.caption("© 2026 SBI Loan Eligibility Prototype | Built with Streamlit")
