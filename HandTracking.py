import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 700

class HandTracking:
    def __init__(self):
        self.hand_tracking = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.hand_x = 0
        self.hand_y = 0
        self.results = None
        self.hand_closed = False
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT

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

        self.hand_closed = False

        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                x, y = int(hand_landmarks.landmark[9].x * self.screen_width), int(hand_landmarks.landmark[9].y * self.screen_height)
                self.hand_x, self.hand_y = x, y

                x1, y1 = int(hand_landmarks.landmark[12].x * self.screen_width), int(hand_landmarks.landmark[12].y * self.screen_height)

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
        return self.hand_x, self.hand_y

    def display_hand(self, image):
        cv2.imshow("image", image)
        cv2.waitKey(1)