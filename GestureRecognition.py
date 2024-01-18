import cv2
import mediapipe as mp

class GestureRecognition:
    def __init__(self, width=1280, height=720):
        self.hand_tracking = mp.solutions.hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.screen_width = width
        self.screen_height = height
        self.cap = cv2.VideoCapture(0)

    def set_screensize(self, width, height):
        self.screen_width = width
        self.screen_height = height

    def _load_camera(self):
        _, self.frame = self.cap.read()

    def scan_hands(self):
        ret, frame = self.cap.read()
        if ret:
            rows, cols, _ = frame.shape

            frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
            frame.flags.writeable = False
            self.results = self.hand_tracking.process(frame)

            frame.flags.writeable = True
            self.frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    def show_image(self):
        cv2.imshow("Frame", self.frame)
        cv2.waitKey(1)

    def display_hand(self):
        cv2.imshow("image", self.frame)
        cv2.waitKey(1)

    def release_camera(self):
        self.cap.release()
        cv2.destroyAllWindows()

# Beispiel-Nutzung der Klasse:
hand_detection = GestureRecognition(width=1280, height=720)
hand_detection.set_screensize(1280, 720)
hand_detection._load_camera()
hand_detection.scan_hands()
hand_detection.show_image()
hand_detection.display_hand()
hand_detection.release_camera()
