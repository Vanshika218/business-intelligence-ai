import streamlit as st
from services.email_service import send_email


def show_email(report_pdf):

    st.divider()

    st.subheader("📧 Email Business Report")

    email = st.text_input(
        "Recipient Email",
        placeholder="example@gmail.com"
    )

    if st.button("📤 Send Report"):

        if email == "":
            st.warning("Please enter an email address.")

        else:

            try:

                send_email(
                    receiver_email=email,
                    pdf_path=report_pdf
                )

                st.success("Report sent successfully!")

            except Exception as e:

                st.error(f"Failed to send email.\n\n{e}")