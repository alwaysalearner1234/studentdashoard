import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 Student Performance Dashboard")
st.write("Interactive analysis of student academic performance")

# Load dataset
df = pd.read_csv("students.csv")

# Calculate average
df["Average"] = (
    df["Maths"] +
    df["Python"] +
    df["DataScience"]
) / 3

# Round average
df["Average"] = df["Average"].round(2)

# Sidebar
st.sidebar.header("🔍 Filters")

department = st.sidebar.selectbox(
    "Select Department",
    ["All"] + list(df["Department"].unique())
)

# Apply filter
if department != "All":
    filtered_df = df[df["Department"] == department]
else:
    filtered_df = df

# Dashboard metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "👨‍🎓 Students",
        len(filtered_df)
    )

with col2:
    st.metric(
        "📈 Average Score",
        round(filtered_df["Average"].mean(), 2)
    )

with col3:
    st.metric(
        "📝 Best Score",
        round(filtered_df["Average"].max(), 2)
    )

with col4:
    st.metric(
        "📅 Avg Attendance",
        f"{round(filtered_df['Attendance'].mean(), 2)}%"
    )

st.divider()

# Chart 1
st.subheader("📚 Subject Performance")

subject_average = pd.DataFrame({
    "Subject": ["Maths", "Python", "Data Science"],
    "Average": [
        filtered_df["Maths"].mean(),
        filtered_df["Python"].mean(),
        filtered_df["DataScience"].mean()
    ]
})

fig1 = px.bar(
    subject_average,
    x="Subject",
    y="Average",
    title="Average Score by Subject",
    text_auto=".2f"
)

st.plotly_chart(fig1, use_container_width=True)

# Chart 2
st.subheader("👨‍🎓 Student Performance")

fig2 = px.bar(
    filtered_df,
    x="Name",
    y="Average",
    title="Average Score of Students",
    text_auto=".2f"
)

st.plotly_chart(fig2, use_container_width=True)

# Chart 3
st.subheader("📅 Attendance vs Performance")

fig3 = px.scatter(
    filtered_df,
    x="Attendance",
    y="Average",
    text="Name",
    title="Attendance vs Average Score",
    size="Average"
)

st.plotly_chart(fig3, use_container_width=True)

# Student table
st.subheader("📋 Student Details")

st.dataframe(
    filtered_df,
    use_container_width=True
)