import streamlit as st


def show_footer():

    st.divider()

    st.markdown(
        """
        <div style="text-align:center;color:gray;">
        Developed by <b>Vanshika Agarwal</b><br>
        AI Business Intelligence Platform
        </div>
        """,
        unsafe_allow_html=True
    )