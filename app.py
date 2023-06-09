#UseCase: Find the largest among the 3 given numbers(value greater than the other two).

import streamlit as st
import pandas as pd
import pickle
st.write("""Find the largest among the 3 given numbers(value greater than the other two)""")
st.header('Input the Three numbers you want')
def user_input_features():
    first_number = st.number_input("Enter the first number",step=1)
    second_number = st.number_input("Enter the second number",step=1)
    third_number = st.number_input("Enter the third number",step=1)
    data = {'Numbers': [first_number,second_number,third_number]}
    return data
df = user_input_features()
max_number = max(df['Numbers'])
st.header(':red[Result]')
st.subheader(f'The Largest among the three numbers is {max_number}')
