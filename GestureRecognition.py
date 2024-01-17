import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

class GestureRecognition:
    def __init__(self, width, height):
        # Load camera
        self.hand_tracking = HandTracking()
        self.hand_tracking.set_screensize(width, height)
        self.cap = cv2.VideoCapture(0)
        self.handpos = (0, 0)
        self.hand_closed = False
        self.image = None
        
    def _load_camera(self):
        _, self.frame = self.cap.read()
        
    def detect(self):
        self._load_camera()
        self.image = self.hand_tracking.scan_hands(self.frame)
        self.hand_pos = self.hand_tracking.get_hand_center()
        self.hand_closed =  self.hand_tracking.hand_closed
        
    def show_image(self):
        cv2.imshow("Frame", self.image)
        cv2.waitKey(1)
        
        
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 700

class HandTracking:
    def __init__(self):
        self.hand_tracking = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.hand_x = 0
        self.hand_y = 0
        self.results = None
        self.hand_closed = False
        self.screen_with = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT

    def set_screensize(self, width, height):
        self.screen_with = width
        self.screen_height = height

    def scan_hands(self, image):
        rows, cols, _ = image.shape

        # Flip the image horizontally for a later selfie-view display, and convert
        # the BGR image to RGB.
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        self.results = self.hand_tracking.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        self.hand_closed = False

        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                x, y = hand_landmarks.landmark[9].x, hand_landmarks.landmark[9].y

                self.hand_x = int(x * self.screen_with)
                self.hand_y = int(y * self.screen_height)

                x1, y1 = hand_landmarks.landmark[12].x, hand_landmarks.landmark[12].y

                if y1 > y:
                    self.hand_closed = True

                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
        return image

    def get_hand_center(self):
        return (self.hand_x, self.hand_y)


    def display_hand(self):
        cv2.imshow("image", self.image)
        cv2.waitKey(1)



