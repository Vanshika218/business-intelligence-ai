import streamlit as st
from services.forecast_service import predict_next_revenue


def show_forecast(sales):

    prediction = predict_next_revenue(
        sales["revenue_trend"]
    )

    st.subheader("📈 AI Revenue Forecast")

    st.metric(
        "Predicted Next Revenue",
        f"₹{prediction:,.0f}"
    )

    st.info(
        f"""
Based on historical sales, the estimated revenue for the next period is

### ₹{prediction:,.0f}

This prediction uses a Linear Regression forecasting model.
"""
    )