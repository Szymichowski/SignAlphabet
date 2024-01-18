# main.py

import tkinter as tk
from PIL import Image, ImageTk
from GestureRecognition import GestureRecognition

class CameraApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        # GestureRecognition-Objekt erstellen
        self.hand_detection = GestureRecognition(1280, 720)  # Breite und Höhe entsprechend anpassen

        # Tkinter Canvas für Videoanzeige erstellen
        self.canvas = tk.Canvas(window)
        self.canvas.pack(expand=True, fill=tk.BOTH)

        # Button zum Schließen des Programms hinzufügen
        self.close_button = tk.Button(window, text="Schließen", command=self.close_app)
        self.close_button.pack()

        # GUI-Aktualisierung starten
        self.update()

    def update(self):
        # Frame von der Kamera lesen und Hand scannen
        self.hand_detection.scan_hands()

        # Aktualisiere das Tkinter Canvas mit dem neuen Frame
        photo = ImageTk.PhotoImage(image=Image.fromarray(self.hand_detection.frame))
        self.canvas.config(width=self.hand_detection.frame.shape[1], height=self.hand_detection.frame.shape[0])
        self.canvas.create_image(0, 0, image=photo, anchor=tk.NW)
        self.canvas.photo = photo  # Referenz behalten, um das Bild vor dem Garbage Collection zu schützen

        # GUI-Aktualisierung rekursiv fortsetzen
        self.window.after(10, self.update)

    def close_app(self):
        # Beende die Videoaufnahme und schließe die GUI
        self.hand_detection.release_camera()
        self.window.destroy()

# Hauptprogramm
root = tk.Tk()
root.resizable(False, False)
app = CameraApp(root, "Kamera GUI")
root.mainloop()