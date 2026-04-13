import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Config
st.set_page_config(page_title="SBI Loan Dashboard", layout="wide")

# Custom CSS (Dark Dashboard Style)
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
h1, h2, h3, h4 {
    color: #ffffff;
}
.metric-box {
    background-color: #161b22;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align:center; color:#ff9933;'>STATE BANK OF INDIA</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center;'>🏦 Loan Eligibility Dashboard</h2>", unsafe_allow_html=True)
st.write("")

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

# Eligibility Logic
def check_eligibility(income, loan_amount, credit_score, age):
    if age < 21:
        return "Not Eligible"
    if credit_score < 650:
        return "Not Eligible"
    if income < 25000:
        return "Not Eligible"
    if loan_amount > income * 20:
        return "Not Eligible"
    return "Eligible"

# Button
if st.button("Check Eligibility"):
    result = check_eligibility(income, loan_amount, credit_score, age)

    if result == "Eligible":
        st.success("✅ You are eligible for the loan")
    else:
        st.error("❌ You are not eligible")

st.markdown("---")

# Graph Section
st.subheader("📊 Loan Trend Analysis")

data = pd.DataFrame({
    "Days": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Applications": [50, 70, 65, 80, 90, 120, 100]
})

fig, ax = plt.subplots()
ax.plot(data["Days"], data["Applications"], marker='o')
ax.set_xlabel("Days")
ax.set_ylabel("Applications")
ax.set_title("Weekly Loan Applications")

st.pyplot(fig)

# Footer
st.markdown("---")
st.caption("© 2026 SBI Loan Eligibility Prototype | Built with Streamlit")
