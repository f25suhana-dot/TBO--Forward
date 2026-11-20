from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="TBO Forward Planner", layout="wide")

# Hide Streamlit's default padding, header and footer so the prototype fills the page
st.markdown(
    """
    <style>
      .block-container {padding: 0 !important; max-width: 100% !important;}
      header, footer, #MainMenu {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = Path(__file__).parent.joinpath("index.html").read_text(encoding="utf-8")

# components.html runs the page's JavaScript (st.html does not)
components.html(html, height=2600, scrolling=True)
