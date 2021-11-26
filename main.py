from re import T
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


st.title('Streamlit 入門')

st.write('Display Image')

option = st.text_input(
    'あなたが好きなスポーツを教えてください',
    
)

'あなたの好きなスポーツは',option,'です'
# if st.checkbox('Show Image'):
#     img = Image.open('/home/sense_iy/main.py/2_l.jpg　バイオハザード　レオン')
#     st.image(img, caption='wasabi', use_column_width=True)

