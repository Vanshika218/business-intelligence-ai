import streamlit as st

from utils.charts import (
    revenue_chart,
    revenue_trend_chart,
    inventory_chart
)


def show_dashboard(sales, inventory, product):

    st.subheader("📊 Business Dashboard")

    revenue_df = sales["revenue_by_product"].copy()

    inventory_df = inventory["inventory_df"].copy()

    if product != "All Products":

        revenue_df = revenue_df[
            revenue_df["Product"] == product
        ]

        inventory_df = inventory_df[
            inventory_df["Product"] == product
        ]

    col1, col2 = st.columns(2)

    with col1:

        st.plotly_chart(
            revenue_chart(revenue_df),
            use_container_width=True
        )

    with col2:

        st.plotly_chart(
            revenue_trend_chart(
                sales["revenue_trend"]
            ),
            use_container_width=True
        )

    st.divider()

    st.subheader("📦 Inventory Status")

    st.plotly_chart(
        inventory_chart(inventory_df),
        use_container_width=True
    )