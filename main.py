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



