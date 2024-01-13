import cv2
from Signs.BaseGesture import BaseGesture


class SignLanguageInterpreter:
    def __init__(self):
        self.a_gesture = Gesture()

    def detect_letter(self, frame):
        # Implementation of Logi, for recognition of the letter classes
        if self.a_gesture.detect_gesture(frame):
            return 'A'
        elif self.b_gesture.detect_gesture(frame):
            return 'B'
        elif self.b_gesture.detect_gesture(frame):
            return 'B'

        # Return, if no letter is detected
        return None
