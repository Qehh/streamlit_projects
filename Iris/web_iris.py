# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 20:23:21 2021

@author: Qehh
"""

import streamlit as st
import joblib
from PIL import Image

st.title('Определение вида ириса по параметрам околоцветника')

'''
## определяем цветок :sunglasses:

'''

model = joblib.load('Iris/model_lr_downloaded.joblib') # загрузка модели

SepalLength = st.slider('Sepal Length, cm', min_value=4.3, max_value=7.9, value=5.0, step=0.1)
SepalWidth = st.slider('Sepal Width, cm,', min_value=2.0, max_value=4.4, value=2.2, step=0.1)
PetalLength = st.slider('Petal Length, cm', min_value=1.0, max_value=6.9, value=3.2, step=0.1)
PetalWidth = st.slider('Petal Width, cm', min_value=0.1, max_value=2.5, value=1.5, step=0.1)


iris_type = model.predict([[SepalLength, SepalWidth, PetalLength, PetalWidth]])
#st.write('## Тип цветка: ', iris_type[0])

if iris_type[0] == 'Iris-setosa':
    image = Image.open('Iris/iris-setosa.jpg')
    st.image(image)
    
if iris_type[0] == 'Iris-versicolor':
    image = Image.open('Iris/iris-versicolor.jpg')
    st.image(image)
    
if iris_type[0] == 'Iris-virginica':
    image = Image.open('Iris/iris-virginica.jpg')
    st.image(image)


