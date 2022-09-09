import streamlit as st
import cv2

import numpy as np
# function used to segmented the image by kmean


def segmentation(image):
    # convert BGR image to RGB
    image = cv2.imread(image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    transformed = image.reshape((-1, 3))
    transformed = np.float32(transformed)
    k = 4  # determine number of clusters
    attempts = 10
    crtieria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
    ret, label, center = cv2.kmeans(
        transformed, k, None, crtieria, attempts, cv2.KMEANS_PP_CENTERS)
    center = np.uint8(center)
    result = center[label.flatten()]
    result_image = result.reshape((image.shape))

    return result_image
