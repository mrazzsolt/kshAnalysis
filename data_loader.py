import pandas as pd  # A pandas könyvtárat használjuk a DataFrame kezeléséhez és CSV fájlok beolvasásához
import chardet  # A chardet könyvtárat a fájl kódolásának automatikus detektálásához használjuk

class DataLoader:  # Egy osztály a CSV adatok beolvasására és előkészítésére
    def __init__(self, file_path):  # Konstruktor, amely inicializálja az osztály változóit
        self.file_path = file_path  # A beolvasandó fájl elérési útja
        self.data = None  # Az adatokat tároló változó, kezdetben None

    def detect_encoding(self):
        #Automatikusan detektálja a fájl kódolását
        with open(self.file_path, 'rb') as f:  # Megnyitja a fájlt bináris módban
            result = chardet.detect(f.read())  # Detektálja a fájl kódolását a teljes fájl tartalmán
            return result['encoding']  # Visszaadja a detektált kódolást
        
    def load_data(self):
        #Beolvassa a CSV fájlt a megfelelő kódolással és visszaadja a DataFrame-et
        encoding = self.detect_encoding()  # Meghívja a kódolás detektálását és eltárolja
        try:
            # CSV fájl beolvasása, a kódolás figyelembevételével. A "sep=';'"" megadja, hogy az oszlopokat pontosvessző választja el.
            # 'skiprows=1' pedig az első sort kihagyja.
            self.data = pd.read_csv(self.file_path, sep=';', skiprows=1, encoding=encoding)
            
            # Adatok tisztítása: a 'Használt lakás', 'ÚJ lakás', 'Összesen' oszlopban lévő szóközöket eltávolítjuk, majd floattá alakítjuk
            self.data['Használt lakás'] = self.data['Használt lakás'].str.replace(' ', '').astype(float)
            self.data['Új lakás'] = self.data['Új lakás'].str.replace(' ', '').astype(float)
            self.data['Összesen'] = self.data['Összesen'].str.replace(' ', '').astype(float)

            print(f"Adatok sikeresen beolvasva a következő kódolással: {encoding}")

        except UnicodeDecodeError as e:  # Ha a kódolás nem megfelelő, UnicodeDecodeError keletkezik
            print(f"Nem sikerült a fájl beolvasása az {encoding} kódolással. Hiba: {e}")
        return self.data  # Visszaadja a beolvasott és feldolgozott adatokat tartalmazó DataFrame-et