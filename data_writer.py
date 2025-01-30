import pandas as pd  # Pandas könytvtár importálása
class DataWriter:  # Egy osztály a CSV adatok kiíratására
    def __init__(self, file_path, data):  # Konstruktor, amely inicializálja az osztály változóit
        self.file_path = file_path  # A kiírandó fájl helye
        self.data = data  # Az adatokat tároló változó
    def write_out(self):
        try:
            if isinstance(self.data,pd.DataFrame):
                self.data.to_csv(self.file_path,index=False,encoding='utf-8')
                print(f"Az adatok sikeresen kiírva: {self.file_path}")
            else:
                print("Hiba: A bemenet nem Pandas DataFrame típusú")
        except Exception as e:
            print(f"Hiba történt a fájl kiírása közben: {e}")