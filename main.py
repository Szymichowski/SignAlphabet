import PySimpleGUI as sg
import cv2
from CameraRecognition import CameraRecognition

class SignLanguageApp:
    def __init__(self):
        # Die Kameraklasse initialisieren
        self.camera_recognition = CameraRecognition()

        # Layout der GUI definieren
        layout = [
            [sg.Image(filename='', key='-IMAGE-')],
            [sg.Button('Start Gesture Recognition')],
            [sg.Text('Detected Letter:'), sg.Text('', key='-LETTER-')],
            [sg.Button('Exit')]
        ]

        # Fenster erstellen
        self.window = sg.Window('Sign Language Recognition', layout, finalize=True, resizable=True)

    def update_detected_letter(self, letter):
        # Aktualisiere den angezeigten Buchstaben
        self.window['-LETTER-'].update(letter)

    def close(self):
        # Schließe die GUI
        self.window.close()

# Beispiel für die Verwendung der GUI
if __name__ == '__main__':
    app = SignLanguageApp()

    while True:
        event, values = app.window.read()

        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        elif event == 'Start Gesture Recognition':
            # Hier kannst du die Gestenerkennung starten und den erkannten Buchstaben aktualisieren
            detected_letter = 'A'  # Beispielwert, ersetze dies mit der tatsächlichen Logik
            app.update_detected_letter(detected_letter)

    app.close()
