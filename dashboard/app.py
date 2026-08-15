import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="UrbanCool AI",
    page_icon="🏙️",
    layout="wide"
)

html_file = Path(__file__).parent / "UrbanCool_AI_single_dashboard.html"

if not html_file.exists():
    st.error("UrbanCool_AI_single_dashboard.html not found.")
    st.stop()

html_content = html_file.read_text(encoding="utf-8")

components.html(
    html_content,
    height=1200,
    scrolling=True
)