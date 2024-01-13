import PySimpleGUI as sg

class YourGUI:
    def __init__(self):
        # Layout der GUI definieren
        layout = [
            [sg.Button('Start Gesture Recognition')],
            [sg.Text('Detected Letter:'), sg.Text('', key='-LETTER-')]
        ]

        # Fenster erstellen
        self.window = sg.Window('Sign Language Recognition', layout, finalize=True)

    def update_detected_letter(self, letter):
        # Aktualisiere den angezeigten Buchstaben
        self.window['-LETTER-'].update(letter)

    def close(self):
        # Schließe die GUI
        self.window.close()

# Beispiel für die Verwendung der GUI
if __name__ == '__main__':
    your_gui = YourGUI()

    while True:
        event, values = your_gui.window.read()

        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Start Gesture Recognition':
            # Hier kannst du die Gestenerkennung starten und den erkannten Buchstaben aktualisieren
            detected_letter = 'A'  # Beispielwert, ersetze dies mit der tatsächlichen Logik
            your_gui.update_detected_letter(detected_letter)

    your_gui.close()
