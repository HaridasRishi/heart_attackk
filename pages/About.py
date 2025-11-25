import streamlit as st
from utils import set_theme, card_container
set_theme()

def about():
    st.markdown('<h2 style="color:#1F2937">About this app</h2>', unsafe_allow_html=True)
    st.write('This Streamlit app was converted from a Flask-based project. Use the Predict page to enter patient data and get predictions.')
    st.markdown('''
**Deployment instructions**
1. Push this repository to GitHub.
2. On Streamlit Cloud (https://share.streamlit.io/) create a new app and point it to this repository's `app.py` file.
3. Ensure `requirements.txt` includes all dependencies and (optionally) include your own `model.pkl` for real predictions.
''')
card_container(about)
