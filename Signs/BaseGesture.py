class BaseGesture:
    def __init__(self):
        # Gemeinsame Initialisierung für alle Gesten
        pass

    def detect_gesture(self, frame):
        # Gemeinsame Logik für die Gestenerkennung
        pass

class AGesture(BaseGesture):
    def __init__(self):
        super().__init__()
        # Spezifische Initialisierung für den Buchstaben A

    def detect_gesture(self, frame):
        # Spezifische Logik für die A-Gestenerkennung
        pass

class BGesture(BaseGesture):
    # Hier würdest du die Klasse für den Buchstaben B implementieren

# Ähnlich würdest du für die anderen Buchstabenklassen vorgehen.
