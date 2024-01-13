import cv2

class CameraRecognition:
    def __init__(self, camera_index=0):
        # Initialisierung der Kameraerkennung
        self.capture = cv2.VideoCapture(camera_index)

    def get_frame(self):
        # Einzelbild von der Kamera erhalten
        ret, frame = self.capture.read()
        if ret:
            return frame
        else:
            return None

    def release(self):
        # Freigabe der Kameraressourcen
        self.capture.release()
