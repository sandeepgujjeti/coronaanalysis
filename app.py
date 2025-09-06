import os
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# ✅ Check current working directory
st.write("Current working directory:", os.getcwd())

# ✅ Full path to your dataset
file_path = r"C:\Users\bittu\OneDrive\certificates\Projects\Corona analysis\covid_data.csv"

# ✅ Load dataset safely
try:
    data = pd.read_csv(file_path)
    st.success("Dataset loaded successfully!")
except FileNotFoundError:
    st.error(f"File not found: {file_path}")
    st.stop()

# ✅ Show first 5 rows
st.subheader("Preview of Dataset")
st.write(data.head())

# ------------------------------
# 📊 Basic Information
# ------------------------------
st.subheader("Dataset Info")
st.write("Number of Rows:", data.shape[0])
st.write("Number of Columns:", data.shape[1])
st.write("Columns:", list(data.columns))

# ------------------------------
# 📈 Line Chart (Cases Over Time)
# ------------------------------
if "Date" in data.columns and "Cases" in data.columns:
    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
    data = data.dropna(subset=["Date"])  # remove invalid dates
    data = data.sort_values("Date")

    st.subheader("COVID-19 Cases Over Time")
    st.line_chart(data.set_index("Date")["Cases"])
else:
    st.warning("Dataset missing 'Date' or 'Cases' column.")

# ------------------------------
# 🥧 Pie Chart (Vaccination Data)
# ------------------------------
if "India COVID-19 Data" in data.columns and "Value" in data.columns:
    vacc_data = data[["India COVID-19 Data", "Value"]].dropna()
    vacc_data = vacc_data[vacc_data["Value"] > 0]

    fig, ax1 = plt.subplots()
    ax1.pie(
        vacc_data["Value"],
        labels=vacc_data["India COVID-19 Data"],
        autopct="%1.1f%%",
        startangle=90,
    )
    ax1.axis("equal")
    st.subheader("Vaccination Data Distribution")
    st.pyplot(fig)
else:
    st.warning("Dataset missing 'India COVID-19 Data' or 'Value' column.")

# ------------------------------
# 📊 Bar Chart (Top 10 States by Cases)
# ------------------------------
if "State" in data.columns and "Cases" in data.columns:
    state_cases = data.groupby("State")["Cases"].sum().sort_values(ascending=False).head(10)

    st.subheader("Top 10 States by Cases")
    st.bar_chart(state_cases)
else:
    st.warning("Dataset missing 'State' or 'Cases' column.")
