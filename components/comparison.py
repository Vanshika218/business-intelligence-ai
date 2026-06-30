import streamlit as st
from services.history_service import calculate_growth


def show_comparison(sales):

    previous_revenue = sales["total_revenue"] * 0.85

    growth = calculate_growth(
        sales["total_revenue"],
        previous_revenue
    )

    st.subheader("📈 Business Growth")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Current Revenue",
            f"₹{sales['total_revenue']:,}",
            f"{growth}%"
        )

    with col2:
        st.metric(
            "Previous Revenue",
            f"₹{int(previous_revenue):,}"
        )