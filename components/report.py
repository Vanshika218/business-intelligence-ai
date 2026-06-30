import streamlit as st
from utils.export_pdf import create_pdf


def show_report(report, sales, inventory, reviews):

    st.divider()

    st.subheader("🤖 AI Business Report")

    st.markdown(report)

    pdf_path = create_pdf(report)

    with open(pdf_path, "rb") as file:

        st.download_button(
            label="📄 Download PDF Report",
            data=file,
            file_name="Business_Report.pdf",
            mime="application/pdf"
        )

    return pdf_path