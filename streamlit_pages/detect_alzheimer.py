import streamlit as st
import cv2
import numpy as np
import joblib
import pandas as pd
import time
from keras.models import load_model


def alzheimer_detection():
    class AlzheimerDetection:
        def __init__(self):
            pass

        def preprocess_image(self, image_path):
            img = cv2.imread(image_path)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray = gray / 255
            gray = cv2.resize(gray, (200, 200))
            processed_img = gray.reshape(1, 200, 200, 1)
            return processed_img

        def predict_alzheimer(self, image_path, model):
            processed_img = self.preprocess_image(image_path)
            prediction = model.predict(processed_img)
            class_label = np.argmax(prediction)
            classes = ["AD (Alzheimer's Disease)", "CN (Cognitively Normal)", 
                       "EMCI (Early Mild Cognitive Impairment)",
                       "LMCI (Late Mild Cognitive Impairment)", 
                       "MCI (Mild Cognitive Impairment)"]
            return classes[class_label]

        def run(self, model):
            st.title("Alzheimer Detection")
            st.write("Upload an image for Alzheimer detection")
            uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg"])

            if uploaded_file is not None:
                image_path = "temp.jpg"
                with open(image_path, "wb") as f:
                    f.write(uploaded_file.getvalue())
                st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
                predict_button = st.button("Predict")

                if predict_button:
                    st.write("Predicting...")
                    with st.spinner('Predicting...'):
                        time.sleep(2)
                        result = self.predict_alzheimer(image_path, model)
                    st.write("Predicted class:", result)

    alzheimer_detector = AlzheimerDetection()
    model = load_model(r"your_model_name.h5")
    alzheimer_detector.run(model)


