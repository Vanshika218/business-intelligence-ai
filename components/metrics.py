import streamlit as st


def show_metrics(sales, reviews):

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "💰 Revenue",
        f"₹{sales['total_revenue']:,}"
    )

    col2.metric(
        "📦 Units Sold",
        sales["total_units"]
    )

    col3.metric(
        "⭐ Top Product",
        sales["top_product"]
    )

    col4.metric(
        "😊 Satisfaction",
        f"{reviews['positive_percentage']}%"
    )