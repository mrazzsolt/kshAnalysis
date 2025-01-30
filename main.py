import tkinter as tk  # A tkinter modul importálása a GUI létrehozásához
from tkinter import messagebox  # Az üzenetablak funkciók importálása
from data_loader import DataLoader  # Az adatbetöltő osztály importálása
from data_analyzer import DataAnalyzer  # Az adatelemző osztály importálása
from data_visualizer import DataVisualizer  # Az adatvizualizáló osztály importálása
from data_writer import DataWriter  # Az adatíró osztály importálása

# Az alkalmazás osztály definiálása
class DataApp:
    def __init__(self, root):  # Konstruktor a főablak inicializálásához
        self.root = root  # A főablak tárolása
        self.root.title("Beadandó")  # Az ablak címének beállítása
        self.data = None  # Az adatok tárolására használt változó
        self.setup_gui()  # A grafikus felület beállítása

    def setup_gui(self):  # A GUI elemek beállításához használt metódus
        frame = tk.Frame(self.root, padx=20, pady=20)  # Keret létrehozása az elrendezéshez
        frame.pack()  # A keret csomagolása
        # Elemző gomb és címke létrehozása
        analyze_label = tk.Label(frame, text="Az adatok statisztikai analizálása:")  # Címke szöveggel
        analyze_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)  # A címke elhelyezése
        analyze_button = tk.Button(frame, text="Statisztika", command=lambda: self.analyze_data(False), width=15, height=1)  # Gomb az elemzéshez
        analyze_button.grid(row=0, column=1, padx=5, pady=5)  # A gomb elhelyezése
        # Elemzés mentése gomb és címke létrehozása
        analyze_save_label = tk.Label(frame, text="Statisztikai adatok mentése:")  # Címke szöveggel
        analyze_save_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)  # A címke elhelyezése
        analyze_save_button = tk.Button(frame, text="Mentés", command=lambda: self.analyze_data(True), width=15, height=1)  # Gomb az elemzéshez
        analyze_save_button.grid(row=1, column=1, padx=5, pady=5)  # A gomb elhelyezése
        # Vizualizáló gomb és címke létrehozása
        plot_label = tk.Label(frame, text="Diagrammok vizuális megjelenítése:")  # Címke szöveggel
        plot_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)  # A címke elhelyezése
        plot_button = tk.Button(frame, text="Diagrammok", command=self.visualize_data, width=15, height=1)  # Gomb a vizualizációhoz
        plot_button.grid(row=2, column=1, padx=5, pady=5)  # A gomb elhelyezése

    # Adatok betöltése fájlból
    def load_data(self, file_path):
        try:
            data_loader = DataLoader(file_path)  # Az adatbetöltő osztály példányosítása
            self.data = data_loader.load_data()  # Adatok betöltése
        except FileNotFoundError:  # Ha a fájl nem található
            messagebox.showerror("Hiba", f"Fájl {file_path} nem található.")  # Hibaüzenet megjelenítése
            return False  # Hibás visszatérési érték
        return True  # Sikeres visszatérési érték

    # Adatok mentése fájlba
    def save_data(self, file_path, data):
        try:
            data_writer = DataWriter(file_path, data)  # Az adatíró osztály példányosítása
            data_writer.write_out()  # Adatok kiírása
        except Exception as e:  # Hibakezelés
            messagebox.showerror("Hiba", f"Hiba a kiírás közben: {e}")  # Hibaüzenet megjelenítése
            return False  # Hibás visszatérési érték
        return True  # Sikeres visszatérési érték
    
    # Adatok elemzése
    def analyze_data(self,save):
        try:
            analyzer = DataAnalyzer(self.data,save)  # Az adatelemző osztály példányosítása
            analyzed_data = analyzer.analyze()  # Az adatok elemzése
            # Az elemzett adatok mentése fájlba
            if save:
                file_out_path = 'output/analyzed_data.csv'  # A mentési útvonal meghatározása
                self.save_data(file_out_path, analyzed_data)  # Az adatok mentése
        except Exception as e:  # Hibakezelés
            messagebox.showerror("Hiba", f"Sikertelen adat elemzés: {e}")  # Hibaüzenet megjelenítése

    # Adatok vizualizációja

    def visualize_data(self):
        try:
            visualizer = DataVisualizer(self.data)  # Az adatvizualizáló osztály példányosítása
            visualizer.line_chart()  # Vonaldiagram létrehozása
            visualizer.scatter_plot()  # Szórásdiagram létrehozása
        except Exception as e:  # Hibakezelés
            messagebox.showerror("Vizualizációs hiba", f"Hiba az adat vizualizálásában: {e}")  # Hibaüzenet megjelenítése

# Főprogram
def main():
    root = tk.Tk()  # Tkinter főablak létrehozása
    app = DataApp(root)  # Az alkalmazás inicializálása
    # Adatok betöltése a bemeneti fájlból
    file_in_path = 'input/data.csv'  # A bemeneti fájl elérési útja
    if not app.load_data(file_in_path):  # Ha az adatbetöltés sikertelen
        return  # Kilépés a programból

    # Adatok mentése strukturált formában
    file_out_path = 'output/structured.csv'  # A mentési fájl elérési útja
    if not app.save_data(file_out_path, app.data):  # Ha az adatmentés sikertelen
        return  # Kilépés a programból
    root.mainloop()  # A fő eseményciklus elindítása

# A program indításának ellenőrzése
if __name__ == "__main__":
    main()  # A főprogram meghívása 