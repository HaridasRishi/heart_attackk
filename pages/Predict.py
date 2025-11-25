import streamlit as st
import numpy as np
import pickle, os
from utils import set_theme, card_container

set_theme()

def predict_ui():

    st.markdown("""
        <div style='text-align:center; padding-bottom: 10px;'>
            <h1 style='color:#2563EB; font-weight:700;'>
                Heart Attack Prediction Model
            </h1>
        </div>
    """, unsafe_allow_html=True)

    def form_content():
        with st.form('predict_form'):
            col1, col2 = st.columns(2, gap='large')

            with col1:
                age = st.number_input('Age (Years)', 1, 120, 53)
                sex = st.selectbox('Sex', ['Male (M)', 'Female (F)'])
                chest_pain = st.selectbox(
                    'Chest Pain Type',
                    ['Typical Angina (TA)','Atypical Angina (ATA)','Non-anginal Pain (NAP)','Asymptomatic (ASY)'])

            with col2:
                resting_bp = st.number_input('Resting Blood Pressure (mm Hg)', 0, 300, 145)
                cholesterol = st.number_input('Cholesterol (mm/dl)', 0, 1000, 230)
                fasting_bs = st.selectbox('Fasting Blood Sugar > 120 mg/dl (1=True,0=False)', [0,1])

            submit = st.form_submit_button('Predict Heart Attack', use_container_width=True)

        if submit:
            def map_sex(x): return 1 if 'Male' in x else 0
            def map_cp(x): return {
                'Typical Angina (TA)':0,'Atypical Angina (ATA)':1,'Non-anginal Pain (NAP)':2,'Asymptomatic (ASY)':3
            }.get(x,0)

            features = np.array([
                age,
                map_sex(sex),
                map_cp(chest_pain),
                resting_bp,
                cholesterol,
                fasting_bs
            ]).reshape(1, -1)

            model_path='model.pkl'

            if os.path.exists(model_path):
                try:
                    with open(model_path,'rb') as f:
                        model=pickle.load(f)
                    pred=model.predict(features)[0]
                    st.success(f'Prediction: {pred}')
                except Exception as e:
                    st.error(f'Prediction failed: {e}')
            else:
                st.warning('model.pkl missing. Showing mock output.')
                st.metric('Mock Prediction', float(features.mean()))

    card_container(form_content)

predict_ui()
