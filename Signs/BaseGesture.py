import cv2
import mediapipe as mp

class BaseGesture:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hand_tracking = self.mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.screen_width = 1200  # Standardwerte für Bildschirmgröße, können angepasst werden
        self.screen_height = 700
        self.results = None

    def set_screensize(self, width, height):
        self.screen_width = width
        self.screen_height = height

    def scan_hands(self, image):
        rows, cols, _ = image.shape

        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        self.results = self.hand_tracking.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
