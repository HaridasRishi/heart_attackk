import streamlit as st
from utils import set_theme, card_container

set_theme()

def main_card():
    st.markdown(
        """
        <div style='text-align:center; padding:8px 0 18px 0;'>
          <h1 style='color:#2563EB; margin:0; font-weight:700;'>
            Heart Attack Prediction Model
          </h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style='color:#475569; text-align:center; max-width:820px; margin:0 auto 18px auto;'>
        This is the landing page. Use the <b>Predict</b> page from the sidebar to make predictions.
        </p>
        """,
        unsafe_allow_html=True
    )

card_container(main_card)

st.markdown("---")
st.info("Use the top-left menu (Pages) to open the Predict page.")
