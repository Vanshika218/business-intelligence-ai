import streamlit as st


def show_sidebar():

    st.sidebar.title("📊 Business Intelligence")

    st.sidebar.success("System Ready")

    st.sidebar.divider()

    product = st.sidebar.selectbox(
        "Select Product",
        [
            "All Products",
            "Bedsheet",
            "Comforter",
            "Premium Bedsheet",
            "Luxury Comforter",
            "Cushion Cover"
        ]
    )

    return product