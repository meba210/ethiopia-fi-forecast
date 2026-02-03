import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/processed/ethiopia_fi_enriched.csv")

st.title("Ethiopia Financial Inclusion Dashboard")

st.subheader("Account Ownership Trend")
access = df[df['indicator_code'] == 'ACC_OWNERSHIP']
st.line_chart(access.set_index('observation_date')['value_numeric'])
