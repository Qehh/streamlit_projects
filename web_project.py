import streamlit as st


st.title('Калькулятор квадрата числа')

'''
## вычисляет квадрат числа от 1 до 100

'''

x = st.slider('x')
st.write(x, 'в квадрате =', x * x)

