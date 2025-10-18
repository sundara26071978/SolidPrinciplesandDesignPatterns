class FrenchLocalizer:
    def __init__(self):
        pass
    def localize(self, msg):
        translations = {
            "car": "voiture",
            "bike": "bicyclette",
            "cycle": "cyclette"
        }
        return translations.get(msg, msg)
    
class SpanishLocalizer:
    def __init__(self):
        pass    
    def localize(self, msg):
        translations = {
            "car": "coche",
            "bike": "bicicleta",
            "cycle": "ciclo"
        }
        return translations.get(msg, msg)
    
class EnglishLocalizer:
    def __init__(self):
        pass
    def localize(self, msg):
        return msg
    
if __name__ == "__main__":
    f = FrenchLocalizer()
    e = EnglishLocalizer()
    s = SpanishLocalizer()
    message = ["car", "bike", "cycle"]
    for msg in message:
        print(f.localize(msg))
        print(e.localize(msg))
        print(s.localize(msg))