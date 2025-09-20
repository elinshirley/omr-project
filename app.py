import cv2
import numpy as np
import streamlit as st

st.title("Basic OMR Evaluation System")

# Upload file
uploaded_file = st.file_uploader("Upload OMR Sheet (image)", type=["jpg","png","jpeg"])

# Dummy Answer Key (5 questions)
answer_key = {0:1, 1:2, 2:0, 3:1, 4:3}  

if uploaded_file:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV)

    st.image(thresh, caption="Processed OMR", use_column_width=True)

    # Fake detected answers (just to simulate)
    student_answers = {0:1, 1:2, 2:1, 3:1, 4:3}

    score = 0
    for q in answer_key:
        if answer_key[q] == student_answers[q]:
            score += 1

    st.success(f"Final Score: {score}/{len(answer_key)}")
