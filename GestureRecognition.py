from HandTracking import HandTracking
import cv2

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
        

