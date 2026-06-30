import streamlit as st


def show_summary(sales, inventory, reviews):

    st.subheader("📈 Executive Summary")

    risk = "🟢 Low"

    if len(inventory["low_stock_products"]) >= 3:
        risk = "🟠 Medium"

    if reviews["positive_percentage"] < 40:
        risk = "🔴 High"

    st.info(
        f"""
### Business Snapshot

💰 Revenue : ₹{sales["total_revenue"]:,}

📦 Units Sold : {sales["total_units"]}

⭐ Best Product : {sales["top_product"]}

⚠ Low Stock Products : {len(inventory["low_stock_products"])}

😊 Customer Satisfaction : {reviews["positive_percentage"]}%

🚨 Business Risk : {risk}
"""
    )