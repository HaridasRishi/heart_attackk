import streamlit as st
from utils import set_theme, card_container
set_theme()

def main_card():
    st.markdown(\"\"\"
    <div style='text-align:center; padding:8px 0 18px 0;'>
      <h1 style='color:#2563EB; margin:0; font-weight:700;'>Heart Attack Prediction Model</h1>
    </div>
    \"\"\", unsafe_allow_html=True)
    st.markdown(\"\"\"
    <p style='color:#475569; text-align:center; max-width:820px; margin:0 auto 18px auto;'>
    This is an improved Streamlit conversion of your app. Use the <strong>Predict</strong> page to enter patient data and get a prediction.
    </p>
    \"\"\", unsafe_allow_html=True)

card_container(main_card)
st.markdown('---')
st.info('Use the top-left Pages menu to open the Predict page, or the About page for deployment instructions and the original app backup.')
