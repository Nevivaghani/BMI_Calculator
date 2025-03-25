import streamlit as st
import requests

st.title('Welcome to BMI Calculator')

weight = st.number_input('Enter your weight (in kgs)', min_value=1.0, step=0.1)

status = st.radio('Select your height format:', ('cms', 'meters', 'feet'))

height = st.number_input(f'Enter your height ({status}):', min_value=1.0, step=0.1)

if st.button('Calculate BMI'):
    url = "http://127.0.0.1:8000/bmi_calculator"  

    payload = {"weight": weight, "height": height, "status": status}

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        result = response.json()
        if "error" in result:
            st.error(result["error"])
        else:
            st.text(f"Your BMI Index is {result['bmi']}")
            st.success(f"Category: {result['category']}")
    else:
        st.error("Failed to fetch data from the server.")
