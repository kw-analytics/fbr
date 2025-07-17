import streamlit as st

st.set_page_config(page_title="Army Officers Tax Calculator 2025-26", layout="centered")
st.title("💂‍♂️ Army Officers Income Tax Calculator – FY 2025–26 (Pakistan)")

st.markdown("This app estimates **annual and monthly income tax** based on gross pay, allowances, and exemptions applicable to Army personnel.")

st.header("📥 Enter Monthly Salary Details")

# ---- Helper function for blank text input ----
def get_input(label):
    val = st.text_input(label)
    try:
        return float(val)
    except:
        return 0.0

# ---- Inputs ----
gross_pay = get_input("Gross Pay (PKR)")  # Main change here

hra = get_input("House Rent Allowance (HRA)")
ca = get_input("Conveyance Allowance (CA)")

st.subheader("🛡️ Exempted Allowances")
kit_allowance = st.text_input("Kit Allowance (Exempted)", value="7000")
ration_allowance = st.text_input("Ration Allowance (RA) (Exempted)", value="15000")

# Convert to float safely
try:
    kit_allowance = float(kit_allowance)
except:
    kit_allowance = 0.0

try:
    ration_allowance = float(ration_allowance)
except:
    ration_allowance = 0.0

# ---- Calculations ----
monthly_gross = gross_pay + hra + ca
annual_gross = monthly_gross * 12

# Exemptions
exempt_kit = kit_allowance * 12
exempt_ra = ration_allowance * 12
total_exemptions = exempt_kit + exempt_ra


# Taxable Income
taxable_income = annual_gross - total_exemptions

# ---- Tax Calculation (FY 2025–26 Revised Slabs) ----
def calculate_tax(income):
    if income <= 600000:
        return 0
    elif income <= 1200000:
        return (income - 600000) * 0.01
    elif income <= 2200000:
        return 6000 + (income - 1200000) * 0.11
    elif income <= 3200000:
        return 116000 + (income - 2200000) * 0.23
    elif income <= 4100000:
        return 346000 + (income - 3200000) * 0.30
    else:
        return 616000 + (income - 4100000) * 0.35

annual_tax = calculate_tax(taxable_income)
monthly_tax = round(annual_tax / 12)

# ---- Output ----
st.header("📊 Tax Summary")
st.info(f"**Monthly Tax Deduction:** PKR {monthly_tax:,.0f}")
st.write(f"**Total Monthly Gross Income:** PKR {monthly_gross:,.0f}")
st.write(f"**Annual Gross Income:** PKR {annual_gross:,.0f}")
st.write(f"**Total Annual Exemptions:** PKR {total_exemptions:,.0f}")
st.write(f"**Taxable Income:** PKR {taxable_income:,.0f}")
st.success(f"**Annual Tax Payable:** PKR {annual_tax:,.0f}")
