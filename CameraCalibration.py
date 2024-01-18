import numpy as np
import cv2 as cv
import glob
import pickle

laptop_camera = cv.VideoCapture(0)  # 0 steht für die erste Kamera

# Öffnen der Webcam 1
webcam1 = cv.VideoCapture(1)  # 1 steht für die zweite Kamera

# Öffnen der Webcam 2
webcam2 = cv.VideoCapture(2)  # 2 steht für die dritte Kamera

class CameraCalibration:  # Korrekte Klassenbezeichnung
    def __init__(self, camera_ids, chessboard_sizes, frame_sizes, images_folders, calibration_filenames):
        self.camera_ids = camera_ids
        self.chessboard_sizes = chessboard_sizes
        self.frame_sizes = frame_sizes
        self.images_folders = images_folders
        self.calibration_filenames = calibration_filenames

        # termination criteria
        self.criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

        # prepare object points
        self.objpoints = []
        self.imgpoints = []

        # VideoCapture objects for each camera
        self.cameras = [cv.VideoCapture(i) for i in range(len(self.camera_ids))]

        for chessboard_size in self.chessboard_sizes:
            objp = np.zeros((chessboard_size[0] * chessboard_size[1], 3), np.float32)
            objp[:, :2] = np.mgrid[0:chessboard_size[0], 0:chessboard_size[1]].T.reshape(-1, 2)
            size_of_chessboard_squares_mm = 20
            objp = objp * size_of_chessboard_squares_mm
            self.objpoints.append(objp)

    def resize_frame(self, frame):
        return cv.resize(frame, (1280, 720))

    def calibrate_and_save(self):
        for i, (camera_id, camera, objp) in enumerate(zip(self.camera_ids, self.cameras, self.objpoints)):
            imgpoints = []
            images = glob.glob(self.images_folders[i])

            for image in images:
                ret, frame = camera.read()
                if not ret:
                    print(f"Error reading image from {camera_id}")
                    continue

                frame = self.resize_frame(frame)
                gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                ret, corners = cv.findChessboardCorners(gray, self.chessboard_sizes[i], None)

                if ret:
                    corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), self.criteria)
                    imgpoints.append(corners2)
                    cv.drawChessboardCorners(frame, self.chessboard_sizes[i], corners2, ret)
                    cv.imshow(f'img_{camera_id}', frame)
                    cv.waitKey(1000)

            cv.destroyAllWindows()

            ret, camera_matrix, dist_coeff, rvecs, tvecs = cv.calibrateCamera(objp, imgpoints,
                                                                              self.frame_sizes[i], None, None)

            # Speichern der Kamerakalibrierungsergebnisse für spätere Verwendung
            calibration_data = {'camera_matrix': camera_matrix, 'dist_coefficients': dist_coeff}
            with open(self.calibration_filenames[i], 'wb') as file:
                pickle.dump(calibration_data, file)

        # Release VideoCapture objects
        for camera in self.cameras:
            camera.release()

# Initialisierung der Kameras
camera_ids = ["laptop", "webcam1", "webcam2"]
chessboard_sizes = [(9, 6), (7, 5), (7, 5)]
frame_sizes = [(1280, 720), (1280, 720), (1280, 720)]
images_folders = ['cameraCalibration/images/laptop/*.png',
                   'cameraCalibration/images/webcam1/*.png',
                   'cameraCalibration/images/webcam2/*.png']
calibration_filenames = ["calibration_laptop.pkl", "calibration_webcam1.pkl", "calibration_webcam2.pkl"]

calibrator = CameraCalibration(camera_ids, chessboard_sizes, frame_sizes, images_folders, calibration_filenames)
calibrator.calibrate_and_save()
