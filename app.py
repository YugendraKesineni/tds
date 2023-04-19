#UseCase: Find the largest among the 3 given numbers

import streamlit as st
import pandas as pd
import pickle




st.write("""
# Find Largest Number
This app gives largest number from given three input numbers
""")

st.header('User Input Parameters)

def user_input_features():
    
    
    first_number = st.number_input("Enter the first number and press Enter",step=1)
    second_number = st.number_input("Enter the second number and press Enter",step=1)
    third_number = st.number_input("Enter the third number and press Enter",step=1)
    
    data = {'Numbers': [first_number,second_number,third_number]}
    return data
 
df = user_input_features()
max_number = max(df['Numbers'])

st.header(':red[Result]')
st.subheader(f'The Largest among the three numbers is {max_number}')
