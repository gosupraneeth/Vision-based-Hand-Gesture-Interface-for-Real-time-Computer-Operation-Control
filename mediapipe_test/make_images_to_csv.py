from tkinter.tix import IMAGE
import cv2
import mediapipe as mp
import os
from pathlib import Path
import pandas as pd

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# For static images:
folders = os.listdir('./../dataset_images')
IMAGE_FILES = {}
for folder in folders:
    IMAGE_FILES[folder] = [str(x) for x in Path('./../dataset_images/' + folder).glob("**/*.*")]
#print(IMAGE_FILES)


landmarks = ["WRIST","THUMB_CMC","THUMB_MCP","THUMB_IP","THUMB_TIP","INDEX_FINGER_MCP","INDEX_FINGER_PIP","INDEX_FINGER_DIP","INDEX_FINGER_TIP","MIDDLE_FINGER_MCP","MIDDLE_FINGER_PIP","MIDDLE_FINGER_DIP","MIDDLE_FINGER_TIP","RING_FINGER_MCP","RING_FINGER_PIP","RING_FINGER_DIP","RING_FINGER_TIP","PINKY_MCP","PINKY_PIP","PINKY_DIP","PINKY_TIP"]
columns = ["class_type","wristX","wristY","wristZ","thumb_CmcX","thumb_CmcY","thumb_CmcZ","thumb_McpX","thumb_McpY","thumb_McpZ","thumb_IpX","thumb_IpY","thumb_IpZ","thumb_TipX","thumb_TipY","thumb_TipZ","index_McpX","index_McpY","index_McpZ","index_PipX","index_PipY","index_PipZ","index_DipX","index_DipY","index_DipZ","index_TipX","index_TipY","index_TipZ","middle_McpX","middle_McpY","middle_McpZ","middle_PipX","middle_PipY","middle_PipZ","middle_DipX","middle_DipY","middle_DipZ","middle_TipX","middle_TipY","middle_TipZ","ring_McpX","ring_McpY","ring_McpZ","ring_PipX","ring_PipY","ring_PipZ","ring_DipX","ring_DipY","ring_DipZ","ring_TipX","ring_TipY","ring_TipZ","pinky_McpX","pinky_McpY","pinky_McpZ","pinky_PipX","pinky_PipY","pinky_PipZ","pinky_DipX","pinky_DipY","pinky_DipZ","pinky_TipX","pinky_TipY","pinky_TipZ"]
data = pd.DataFrame(columns=columns)
#print(data)
with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=1,
    min_detection_confidence=0.5) as hands:
    for class_name in IMAGE_FILES.keys():
        for file in IMAGE_FILES[class_name]:
            # Read an image, flip it around y-axis for correct handedness output (see above).
            image = cv2.flip(cv2.imread(file), 1)
            # Convert the BGR image to RGB before processing.
            results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

            # Print handedness and draw hand landmarks on the image.
            #print('Handedness:', results.multi_handedness)
            if not results.multi_hand_landmarks:
                print(file)
                os.remove(file)
                continue

            image_height, image_width, _ = image.shape
            annotated_image = image.copy()
            for hand_landmarks in results.multi_hand_landmarks:
                #print("\n")
                #print('hand_landmarks:', hand_landmarks)
                row = [str(class_name)]
                for land_mark in landmarks:
                    row.append(hand_landmarks.landmark[mp_hands.HandLandmark[land_mark]].x)
                    row.append(hand_landmarks.landmark[mp_hands.HandLandmark[land_mark]].y)
                    row.append(hand_landmarks.landmark[mp_hands.HandLandmark[land_mark]].z)
                    #print(land_mark,hand_landmarks.landmark[mp_hands.HandLandmark[land_mark]].x,hand_landmarks.landmark[mp_hands.HandLandmark[land_mark]].y)
                data.loc[len(data.index)] = row

#print(data)
data.to_csv('data.csv')