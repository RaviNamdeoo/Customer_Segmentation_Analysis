import joblib
import streamlit as st
import pandas as pd

kmeans = joblib.load('artifacts/kmeans_cluster_model.pkl')
scaler = joblib.load('artifacts/scaler.pkl')

st.title("Customer Segmentation Analysis APP")
st.write("Enter Customer details to predict their Segment: ")

age	= st.number_input("Age", min_value=18, max_value=100, value=30)
income	= st.number_input("Income", min_value=0, max_value=200000,value = 50000)
total_spending	= st.number_input("Total Spending made by Customer", min_value = 0, max_value=5000, value=1000)
total_num_purchase	= st.number_input("Number of Total purchases", min_value = 0, max_value=50, value=19)
recency	= st.number_input("Number of Recent visit", min_value=0, max_value=99, value=49)
total_campaign_accepted = st.number_input("Total campaign accepted by the Customer", min_value=0, max_value=4, value=1)

input_data = pd.DataFrame({
    'Age':[age],
    'Income':[income],
    'Total_spending':[total_spending],
    'Total_num_purchase':[total_num_purchase],
    'Recency':[recency],
    'Total_campaign_accepted':[total_campaign_accepted],
})

input_scaled = scaler.transform(input_data)

if st.button('Predict Segment'):
    cluster = kmeans.predict(input_scaled)[0]

    st.success(f'Predicted Segment: {cluster}')
    st.write("""Cluster 0: 'Low Income Low Spenders'\n
                Cluster 1: 'Low Income Least Spenders'\n
                Cluster 2: 'High Age Mid Spenders'\n
                Cluster 3: 'Mid Age High Spenders'\n
                Cluster 4: 'High Income Premium Buyers'\n
                Cluster 5: 'High Age High Spenders
             """)