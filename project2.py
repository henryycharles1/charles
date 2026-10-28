import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import calendar


df = pd.read_csv("NigeriaInflationRates.csv")

df["Month"] = df["Month"].apply(lambda x: calendar.month_name[x])

st.title("Nigeria Inflation Analysis Dashboard")
st.markdown("#### This dashboard analyzes Nigeria's inflation trends, identifies periods of high inflation, examines CPI movements, and explores the relationship between inflation and crude oil prices.")

kpi1, kpi2, kpi3 = st.columns(3)

with kpi1:
    st.metric(label="Average Inflation", value=round(df["Inflation_Rate"].mean(),2))

with kpi2:
    st.metric(label="Year With The Highest Inflation", value=df.groupby("Year")["Inflation_Rate"].mean().idxmax())

with kpi3:
    st.metric(label="Month With The Highest Inflation", value=df["Month"].mode().max())

# kpi4, kpi5 = st.columns(2)
#
# with kpi4:
#     correlation = df["Crude Oil Price"].corr(df["Inflation_Rate"])
#
#     st.metric(label="Oil Price vs Inflation Correlation", value=round(correlation, 2))
#     # st.metric(label="Inflation Price", value=df[["Crude Oil Price", "Inflation_Rate"]].corr())
#
# with kpi5:
#     cpi_columns = ["CPI_Food", "CPI_Energy", "CPI_Health", "CPI_Transport", "CPI_Communication", "CPI_Education"]
#
#     highest_cpi = df[cpi_columns].mean().idxmax()
#
#     st.metric(label="Highest CPI Category", value=highest_cpi)

chart1, chart2 = st.columns(2)

with chart1:
    aver = df.groupby("Month")["Inflation_Rate"].mean()

    fig, ax = plt.subplots()
    aver.plot(kind="line", color="red", ax=ax)
    plt.title("Monthly Inflation_Rate")
    plt.ylabel("Inflation_Rate")
    ax.set_xticks(range(1, 13))
    ax.set_xticklabels([
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ])
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

with chart2:
    year = df.groupby("Year")["Inflation_Rate"].mean()
    fig, ax = plt.subplots()
    year.plot(kind="bar", color="red", ax=ax)
    plt.title("Yearly Inflation_Rate")
    plt.ylabel("Inflation_Rate")
    st.pyplot(fig)

chart3, chart4 = st.columns(2)

with chart3:
    # correlation_price = df["Crude Oil Price"].corr(df["Inflation_Rate"])
    # fig, ax = plt.subplots()
    # ax.bar(["Oil Price vs Inflation"], [correlation_price], color="blue")
    # ax.set_ylabel("Correlation")
    # ax.set_title("Correlation Between Oil Price and Inflation")
    #
    # st.pyplot(fig)
    # Calculate yearly averages
    yearly = df.groupby("Year")[["Inflation_Rate", "Crude Oil Price"]].mean()

    fig, ax1 = plt.subplots(figsize=(10, 5))

    # Inflation rate - left Y-axis
    ax1.plot(yearly.index, yearly["Inflation_Rate"],
             color="red", label="Inflation Rate")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Inflation Rate")

    # Crude oil price - right Y-axis
    ax2 = ax1.twinx()
    ax2.plot(yearly.index, yearly["Crude Oil Price"],
             color="blue", label="Crude Oil Price")
    ax2.set_ylabel("Crude Oil Price")

    plt.title("Yearly Average Inflation Rate vs Crude Oil Price")
    fig.tight_layout()

    st.pyplot(fig)

with chart4:
    fig, ax1 = plt.subplots(figsize=(12, 6))

    cpi_columns = ["CPI_Food", "CPI_Energy", "CPI_Health", "CPI_Transport", "CPI_Communication", "CPI_Education"]

    # First Y-axis
    ax1.plot(df["Year"], df["CPI_Food"], color="red")
    ax1.set_ylabel("Food CPI")

    # second y_axis
    ax2 = ax1.twinx()
    ax2.plot(df["Year"], df["CPI_Energy"], color="blue")
    ax2.set_ylabel("Energy CPI", color="blue")

    ax3 = ax1.twinx()
    ax3.spines["right"].set_position(("outward", 60))
    ax3.plot(df["Year"], df["CPI_Health"], color="green")
    ax3.set_ylabel("Health CPI", color="green")

    ax4 = ax1.twinx()
    ax4.spines["right"].set_position(("outward", 120))
    ax4.plot(df["Year"], df["CPI_Transport"], color="orange")
    ax4.set_ylabel("Transport CPI", color="orange")

    ax5 = ax1.twinx()
    ax5.spines["right"].set_position(("outward", 180))
    ax5.plot(df["Year"], df["CPI_Communication"], color="purple")
    ax5.set_ylabel("Communication CPI", color="purple")

    ax6 = ax1.twinx()
    ax6.spines["right"].set_position(("outward", 240))
    ax6.plot(df["Year"], df["CPI_Education"], color="brown")
    ax6.set_ylabel("Education CPI", color="brown")

    ax1.set_xlabel("Year")
    plt.title("CPI Categories in Nigeria (2008–2024)")
    fig.tight_layout()

    st.pyplot(fig)



st.write("Nigeria Inflation Analysis Dashboard")
st.dataframe(df.head(20))




