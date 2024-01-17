import tkinter as tk
import cv2
from PIL import Image, ImageTk
from GestureRecognition import GestureRecognition

class CameraApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        # OpenCV-Videoaufnahme initialisieren
        self.cap = cv2.VideoCapture(0)

        # Tkinter Canvas für Videoanzeige erstellen
        self.canvas = tk.Canvas(window)
        self.canvas.pack(expand=True, fill=tk.BOTH)

        # Buttons zum Ändern der Programmgröße hinzufügen
        self.make_1080p_button = tk.Button(window, text="1080p", command=self.make_1080p)
        self.make_1080p_button.pack()

        self.make_720p_button = tk.Button(window, text="720p", command=self.make_720p)
        self.make_720p_button.pack()

        # Button zum Schließen des Programms hinzufügen
        self.close_button = tk.Button(window, text="Schließen", command=self.close_app)
        self.close_button.pack()

        # GUI-Aktualisierung starten
        self.update()

    def make_1080p(self):
        self.change_res(1920, 1080)

    def make_720p(self):
        self.change_res(1280, 720)

    def make_480p(self):
        self.change_res(640, 480)

    def change_res(self, width, height):
        self.cap.set(3, width)
        self.cap.set(4, height)

    def update(self):
        # Frame von der Kamera lesen
        ret, frame = self.cap.read()

        # Überprüfe, ob die Frame-Lesung erfolgreich war
        if ret:
            # Aktualisiere das Tkinter Canvas mit dem neuen Frame
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.config(width=frame.shape[1], height=frame.shape[0])
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        # GUI-Aktualisierung rekursiv fortsetzen
        self.window.after(10, self.update)

    def close_app(self):
        # Beende die Videoaufnahme und schließe die GUI
        self.cap.release()
        self.window.destroy()

# Hauptprogramm
root = tk.Tk()
root.resizable(False, False)
app = CameraApp(root, "Kamera GUI")
root.mainloop()





'''
import tkinter as tk
from PIL import Image, ImageTk
import cv2
from GestureRecognition import GestureRecognition

class CameraApp:
    def __init__(self, window, window_title, camera_index=0):
        self.window = window
        self.window.title(window_title)

        # CameraRecognition-Objekt initialisieren
        self.camera_recognition = CameraRecognition(camera_index)

        self.width = 1280
        self.height = 720

        self.create_widgets()

    def create_widgets(self):
        # Tkinter Canvas für Videoanzeige erstellen
        self.canvas = tk.Canvas(self.window)
        self.canvas.pack(expand=True, fill=tk.BOTH)

        # Textfeld für erkannte Buchstaben
        self.text_label = tk.Label(self.window, text="Erkannte Buchstaben:")
        self.text_label.pack()

        self.detected_text = tk.StringVar()
        self.detected_text.set("")
        self.detected_text_label = tk.Label(self.window, textvariable=self.detected_text)
        self.detected_text_label.pack()

        # Button zum Schließen des Programms hinzufügen
        close_button = tk.Button(self.window, text="Schließen", command=self.close_app)
        close_button.pack()

        # GUI-Aktualisierung starten
        self.update()

    def make_720p(self):
        self.camera_recognition.change_res(self.width, self.height)

    def update(self):
        # Frame von der CameraRecognition-Klasse erhalten
        frame = self.camera_recognition.get_frame()

        # Wenn ein Frame vorhanden ist, aktualisiere das Tkinter Canvas mit dem neuen Frame
        if frame is not None:
            frame_rescaled = cv2.resize(frame, (self.width, self.height), interpolation=cv2.INTER_AREA)
            photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame_rescaled, cv2.COLOR_BGR2RGB)))

            self.canvas.config(width=frame_rescaled.shape[1], height=frame_rescaled.shape[0])
            self.canvas.create_image(0, 0, image=photo, anchor=tk.NW)

            # Hier könnte die Buchstabenerkennung eingefügt werden
            # detected_letters = self.camera_recognition.detect_letters(frame)
            # detected_text = "".join(detected_letters)
            # self.detected_text.set(detected_text)

        # GUI-Aktualisierung rekursiv fortsetzen
        self.window.after(10, self.update)

    def close_app(self):
        # Beende die CameraRecognition und schließe die GUI
        self.camera_recognition.release()
        self.window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    
    # CameraApp mit CameraRecognition-Objekt erstellen und die Kamera-Index (default: 0) anpassen, falls erforderlich
    app = CameraApp(root, "Kamera GUI", camera_index=0)
    
    root.mainloop()

'''