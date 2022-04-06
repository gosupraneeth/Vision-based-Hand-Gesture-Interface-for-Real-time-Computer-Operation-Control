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
folders = os.listdir('dataset_images')
IMAGE_FILES = {}
for folder in folders:
    IMAGE_FILES[folder] = [str(x) for x in Path('./../dataset_images/' + folder).glob("**/*.*")]
print(IMAGE_FILES.keys())