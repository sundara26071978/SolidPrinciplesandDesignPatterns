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
    def localize(self, msg):
        return msg
    
def LocalizerFactory(language="English"):
    localizers = {
        "French": FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer,
    }
    return localizers[language]()

if __name__ == "__main__":
    f = LocalizerFactory("French")
    e = LocalizerFactory("English")
    s = LocalizerFactory("Spanish")
    message = ["car", "bike", "cycle"]
    for msg in message:
        print(f.localize(msg))