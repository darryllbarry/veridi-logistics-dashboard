import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df_delivered = pd.read_csv('df_delivered.csv')
state_stats = pd.read_csv('state_stats.csv')
day_stats = pd.read_csv('day_stats.csv')

st.title("Veridi Logistics — Delivery Performance Audit")

# KPIs
st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("On Time %", f"{(df_delivered['delivery_status']=='On Time').mean()*100:.1f}%")
col2.metric("Late %", f"{(df_delivered['delivery_status']=='Late').mean()*100:.1f}%")
col3.metric("Super Late %", f"{(df_delivered['delivery_status']=='Super Late').mean()*100:.1f}%")

# Avg review by status
st.subheader("Avg Review Score by Delivery Status")
review_stats = df_delivered.groupby('delivery_status')['review_score'].mean().round(2)
st.bar_chart(review_stats)

# Late % by state
st.subheader("Late Delivery Rate by State")
fig1, ax1 = plt.subplots(figsize=(10, 8))
ax1.barh(state_stats['customer_state'], state_stats['late_pct'], color='salmon')
ax1.set_xlabel('% Late Deliveries')
ax1.invert_yaxis()
st.pyplot(fig1)

# Late % by day
st.subheader("Late Delivery Rate by Day of Purchase")
fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.bar(day_stats['purchase_day'], day_stats['late_pct'], color='steelblue')
ax2.set_xlabel('Day of Purchase')
ax2.set_ylabel('% Late')
st.pyplot(fig2)