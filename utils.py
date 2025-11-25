import streamlit as st

def set_theme():
    st.set_page_config(page_title='Heart Attack Prediction', layout='centered', page_icon='❤️', initial_sidebar_state='auto')

def card_container(contents_callable):
    with st.container():
        st.markdown(\"\"\"
        <div style="max-width:1100px; margin: 24px auto; padding:28px; background: #ffffff; border-radius: 12px; box-shadow: 0 8px 24px rgba(15,23,42,0.06);">
        \"\"\", unsafe_allow_html=True)
        contents_callable()
        st.markdown(\"\"\"
        </div>
        \"\"\", unsafe_allow_html=True)
