import cv2
import mediapipe as mp
import numpy as np
import streamlit as st
from PIL import Image

import PoseModule as pm

st.title("Pushup Counter")
st.text("This application counts pushups and gives form feedback in real-time.")

# Initialize variables
cap = cv2.VideoCapture(0)
detector = pm.poseDetector()
count = 0
direction = 0
form = 0
feedback = "Fix Form"

stframe = st.empty()

while cap.isOpened():
    ret, img = cap.read()  # 640 x 480

    if not ret:
        st.write("Failed to grab frame")
        break

    # Determine dimensions of video - Help with creation of box in Line 43
    width = cap.get(3)  # float `width`
    height = cap.get(4)  # float `height`
    # print(width, height)

    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    # print(lmList)
    if len(lmList) != 0:
        elbow = detector.findAngle(img, 11, 13, 15)
        shoulder = detector.findAngle(img, 13, 11, 23)
        hip = detector.findAngle(img, 11, 23, 25)

        # Percentage of success of pushup
        per = np.interp(elbow, (90, 160), (0, 100))

        # Bar to show Pushup progress
        bar = np.interp(elbow, (90, 160), (380, 50))

        # Check to ensure right form before starting the program
        if elbow > 160 and shoulder > 40 and hip > 160:
            form = 1

        # Check for full range of motion for the pushup
        if form == 1:
            if per == 0:
                if elbow <= 90 and hip > 160:
                    feedback = "Up"
                    if direction == 0:
                        count += 0.5
                        direction = 1
                else:
                    feedback = "Fix Form"

            if per == 100:
                if elbow > 160 and shoulder > 40 and hip > 160:
                    feedback = "Down"
                    if direction == 1:
                        count += 0.5
                        direction = 0
                else:
                    feedback = "Fix Form"
                    # form = 0

        # Draw Bar
        if form == 1:
            cv2.rectangle(img, (580, 50), (600, 380), (0, 255, 0), 3)
            cv2.rectangle(img, (580, int(bar)), (600, 380), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, f'{int(per)}%', (565, 430), cv2.FONT_HERSHEY_PLAIN, 2,
                        (255, 0, 0), 2)

        # Pushup counter
        cv2.rectangle(img, (0, 380), (100, 480), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (25, 455), cv2.FONT_HERSHEY_PLAIN, 5,
                    (255, 0, 0), 5)

        # Feedback
        cv2.rectangle(img, (500, 0), (640, 40), (255, 255, 255), cv2.FILLED)
        cv2.putText(img, feedback, (500, 40), cv2.FONT_HERSHEY_PLAIN, 2,
                    (0, 255, 0), 2)

    # Convert the image color from BGR to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Display the frame using Streamlit
    stframe.image(img)

cap.release()