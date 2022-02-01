import cv2
import mediapipe as mp
import time


def main():
    cod_x = ""
    cod_y = ""

    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(static_image_mode=False,
                        max_num_hands=2,
                        min_detection_confidence=0.5,
                        min_tracking_confidence=0.5)

    mpDraw = mp.solutions.drawing_utils

    while True:
        success, img = cap.read()
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        lmlist = []
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                x_cod = handLms.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].x
                x_cod *= 100000
                x_cod = int(x_cod)
                x_cod = float(x_cod/100000.0)
                y_cod = handLms.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].y
                y_cod *= 100000
                y_cod = int(y_cod)
                y_cod = float(y_cod/100000.0)
                cod = "x: " + str(x_cod)
                cod += " y: " + str(y_cod)
                cv2.putText(img,cod, (10,100), cv2.FONT_HERSHEY_PLAIN, 2, (255,0,255), 3)

                for id, lm in enumerate(handLms.landmark):
                    #print(id,lm)
                    h, w, c = img.shape
                    cx, cy = int(lm.x *w), int(lm.y*h)
                    lmlist.append([id, cx, cy])
                    #if id ==0:
                    cv2.circle(img, (cx,cy), 3, (255,0,255), cv2.FILLED)

                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

        
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime


        #cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
        
        cv2.imshow("Image",img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()