import streamlit as st
import tempfile

from agents.sales_agent import analyze_sales
from agents.inventory_agent import analyze_inventory
from agents.review_agent import analyze_reviews
from agents.manager_agent import generate_business_report
from components.footer import show_footer
from components.sidebar import show_sidebar
from components.metrics import show_metrics
from components.executive_summary import show_summary
from components.alerts import show_alerts
from components.dashboard import show_dashboard
from components.forecast import show_forecast
from components.comparison import show_comparison
from components.report import show_report
from components.email import show_email
from components.chat import show_chat
from PIL import Image

logo = Image.open("assets/logo.png")

st.image(logo, width=120)

st.set_page_config(
    page_title="AI Business Intelligence Platform",
    page_icon="📊",
    layout="wide"
)

product = show_sidebar()

st.title("📊 AI Business Intelligence Platform")
st.write("Upload your business datasets and let AI generate insights.")

st.divider()

# ==========================
# SESSION STATE
# ==========================

if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

if "sales" not in st.session_state:
    st.session_state.sales = None

if "inventory" not in st.session_state:
    st.session_state.inventory = None

if "reviews" not in st.session_state:
    st.session_state.reviews = None

if "report" not in st.session_state:
    st.session_state.report = None

# ==========================
# FILE UPLOADS
# ==========================

sales_file = st.file_uploader(
    "Upload Sales CSV",
    type=["csv"]
)

inventory_file = st.file_uploader(
    "Upload Inventory CSV",
    type=["csv"]
)

reviews_file = st.file_uploader(
    "Upload Reviews CSV",
    type=["csv"]
)

# ==========================
# ANALYZE BUTTON
# ==========================

if st.button("🚀 Analyze Business"):

    if sales_file and inventory_file and reviews_file:

        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as f:
            f.write(sales_file.getbuffer())
            sales_path = f.name

        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as f:
            f.write(inventory_file.getbuffer())
            inventory_path = f.name

        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as f:
            f.write(reviews_file.getbuffer())
            reviews_path = f.name

        with st.spinner("Analyzing Business..."):

            sales = analyze_sales(sales_path)
            inventory = analyze_inventory(inventory_path)
            reviews = analyze_reviews(reviews_path)

            report = generate_business_report(
                sales,
                inventory,
                reviews
            )

        st.session_state.sales = sales
        st.session_state.inventory = inventory
        st.session_state.reviews = reviews
        st.session_state.report = report
        st.session_state.analysis_done = True

    else:
        st.error("Please upload all three CSV files.")

# ==========================
# SHOW RESULTS
# ==========================

if st.session_state.analysis_done:

    show_metrics(
        st.session_state.sales,
        st.session_state.reviews
    )

    show_summary(
        st.session_state.sales,
        st.session_state.inventory,
        st.session_state.reviews
    )

    show_alerts(
        st.session_state.sales,
        st.session_state.inventory,
        st.session_state.reviews
    )

    show_dashboard(
        st.session_state.sales,
        st.session_state.inventory,
        product
    )

    show_forecast(
        st.session_state.sales
    )

    show_comparison(
        st.session_state.sales
    )

    pdf_path = show_report(
        st.session_state.report,
        st.session_state.sales,
        st.session_state.inventory,
        st.session_state.reviews
    )

    show_email(pdf_path)

    show_chat(
        st.session_state.sales,
        st.session_state.inventory,
        st.session_state.reviews
    )
    show_footer()