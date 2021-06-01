# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 20:23:21 2021

@author: Qehh
"""

import streamlit as st
import joblib
from PIL import Image
# >>> image = Image.open('sunrise.jpg')
# >>>
# >>> st.image(image, caption='Sunrise by the mountains',
# ...          use_column_width=True)


st.title('Определение вида ириса по параметрам околоцветника')
#image = Image.open('iris_photo.jpg')
image = Image.open("c:/Users/Qehh/WebIris/iris_photo.jpg")
st.image(image)

'''
## определяем цветок

'''

model = joblib.load('c:/Users/Qehh/WebIris/model_lr_downloaded.joblib') # загрузка модели

SepalLength = st.slider('Sepal Length, cm', min_value=4.3, max_value=7.9, value=5.0, step=0.1)
SepalWidth = st.slider('Sepal Width, cm,', min_value=2.0, max_value=4.4, value=2.2, step=0.1)
PetalLength = st.slider('Petal Length, cm', min_value=1.0, max_value=6.9, value=3.2, step=0.1)
PetalWidth = st.slider('Petal Width, cm', min_value=0.1, max_value=2.5, value=1.5, step=0.1)


iris_type = model.predict([[SepalLength, SepalWidth, PetalLength, PetalWidth]])
st.write('## Тип цветка: ', iris_type[0])


# # x = st.slider('x', min_value=5.0, max_value=20.0, value=10.0, step=0.1)
# # y = st.slider('y', max_value=35)
# # z = st.slider('z', max_value=55)



# # st.write('# x+y+z =', x+y+z)

# from datetime import datetime
# start_time = st.slider("When do you start?",
#                        value=datetime(2020, 1, 1, 9, 30),
#                        format="MM/DD/YY - hh:mm")
# st.write("Start time:", start_time)