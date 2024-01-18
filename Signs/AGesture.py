import cv2
from BaseGesture import BaseGesture

class AGestureDetector(BaseGesture):
    def __init__(self):
        super().__init__()

    def detect_gesture(self, frame):
        self.scan_hands(frame)

        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

                if self.is_a_gesture(hand_landmarks):
                    return "a"

        return None  # Geste wurde nicht erkannt, daher wird None zurückgegeben

    def is_a_gesture(self, landmarks):
        thumb_tip = landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP]
        index_finger_tip = landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]
        middle_finger_tip = landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]

        # Anpassung: Überprüfe auch, ob der Daumen weiter rechts als der Zeigefinger ist
        if thumb_tip.y > index_finger_tip.y and thumb_tip.y > middle_finger_tip.y and thumb_tip.x > index_finger_tip.x:
            return True
        else:
            return False
