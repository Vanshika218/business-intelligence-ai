import streamlit as st


def show_alerts(sales, inventory, reviews):

    st.subheader("🚨 AI Business Alerts")

    # Critical Inventory Alert
    if len(inventory["low_stock_products"]) > 0:

        st.error(
            f"""
### 🔴 Critical Inventory Alert

The following products are running low on stock:

{', '.join(inventory["low_stock_products"])}

Immediate replenishment is recommended.
"""
        )

    # Customer Satisfaction Alert
    if reviews["positive_percentage"] < 60:

        st.warning(
            f"""
### 🟡 Customer Satisfaction Warning

Positive Review Rate:

{reviews['positive_percentage']}%

Investigate customer complaints and improve service quality.
"""
        )

    # Sales Opportunity
    st.success(
        f"""
### 🟢 Sales Opportunity

Your highest-selling product is:

**{sales['top_product']}**

Consider increasing marketing efforts and maintaining sufficient inventory.
"""
    )