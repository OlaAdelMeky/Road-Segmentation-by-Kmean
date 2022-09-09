from PIL import Image
import numpy as np
import cv2
import streamlit as st
from segmentation import segmentation


st.sidebar.title("ROAD SEGMENTATION")
st.header("Road segmentation")
text = st.text_input("Enter Image Path : ")
if text:
    st.image(text, caption='Orginal Image ', use_column_width=True)

submit = st.button("Segmentation")
if submit:
   
    result = segmentation(text)
   
    st.image(result, caption='Segmentated Image.', use_column_width=True)
    



