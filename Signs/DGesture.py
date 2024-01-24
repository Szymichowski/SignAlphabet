import cv2
import mediapipe as mp
import PySimpleGUI as sg

class BaseGesture:
    def __init__(self):
        pass

    def detect_gesture(self, frame):
        raise NotImplementedError("Subclasses must implement detect_gesture method.")

class DGestureDetector(BaseGesture):
    def __init__(self):
        super().__init__()
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.mp_drawing = mp.solutions.drawing_utils

    def detect_gesture(self, frame):
        result = self.hands.process(frame)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

                if self.is_a_gesture(hand_landmarks):
                    return True

        return False

    def is_a_gesture(self, landmarks):
        thumb_tip = landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP]
        index_finger_tip = landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP]
        middle_finger_tip = landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
        ring_finger_tip = landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP]
        pinkie_finger_tip =landmarks.landmark[self.mp_hands.HandLandmark.PINKIE_FINGER_TIP]

        # Anpassung: Überprüfe auch, ob der Daumen in der Handfläche ist
        if thumb_tip.y < index_finger_tip.y and pinkie_finger_tip.y < index_finger_tip.y and thumb_tip.x > index_finger_tip.x:
            return True
        else:
            return False

def main():
    cap = cv2.VideoCapture(0)
    a_gesture_detector = DGestureDetector()

    # PySimpleGUI GUI erstellen
    layout = [
        [sg.Image(filename='', key='-IMAGE-')],
        [sg.Button('Exit')]
    ]
    window = sg.Window('D Gesture Detection', layout, finalize=True, resizable=True)

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            continue

        frame = cv2.flip(frame, 1)

        if a_gesture_detector.detect_gesture(frame):
            print("OK")

        # Aktualisiere das GUI-Bild
        imgbytes = cv2.imencode('.png', frame)[1].tobytes()
        window['-IMAGE-'].update(data=imgbytes)

        event, values = window.read(timeout=20)

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

    cap.release()
    cv2.destroyAllWindows()
    window.close()

if __name__ == "__main__":
    main()
