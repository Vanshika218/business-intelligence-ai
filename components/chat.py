import streamlit as st
from services.llm_service import generate_response


def show_chat(sales, inventory, reviews):

    st.divider()
    st.subheader("💬 AI Business Assistant")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    question = st.chat_input(
        "Ask anything about your business..."
    )

    if question:

        st.session_state.chat_history.append(
            {
                "role": "user",
                "content": question
            }
        )

        prompt = f"""
You are a Senior Business Intelligence Consultant.

Business Summary

Sales:
{sales}

Inventory:
{inventory}

Reviews:
{reviews}

Answer the user's question professionally.

Question:
{question}
"""

        with st.spinner("Thinking..."):

            try:

                answer = generate_response(prompt)

            except Exception:

                answer = "Sorry, the AI service is temporarily unavailable. Please try again."

        st.session_state.chat_history.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

    for message in st.session_state.chat_history:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])