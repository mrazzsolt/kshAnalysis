import matplotlib.pyplot as plt # Importáljuk a matplotlib.pyplot modult, amely diagramok készítésére szolgál.
import numpy as np # Importáljuk a numpy modult, amely tömbök és matematikai műveletek kezelésére használatos.
from sklearn.linear_model import LinearRegression


class DataVisualizer: # Definiálunk egy osztályt a vizualizációs feladatokhoz. 
    def __init__(self, data): # Az osztály inicializáló függvénye. A konstruktor a bemeneti adatokat tárolja az objektum attribútumában.
        self.data = data  # Az adatokat eltároljuk az objektum self.data attribútumában.
        self.max_y_value = max(self.data['Használt lakás'].max(), self.data['Új lakás'].max()) # Az y-tengely maximális értékét a használt és új lakások adataiból számítjuk.

   # Függvény egy vonaldiagram készítésére.
    def line_chart(self):
       # Vonaldiagram rajzolására szolgáló alakzat méretének beállítása.
        plt.figure(figsize=(10, 12))
        # Vonaldiagram elhelyezése a lap tetején.
        plt.subplot(2, 1, 1)

        # Vonalat rajzolunk a 'Használt lakás' adatok alapján.
        plt.plot(
            self.data['Év'],  # Az x-tengelyre kerülő értékek (évek).
            self.data['Használt lakás'],  # Az y-tengelyre kerülő értékek (használt lakások száma).
            label='Használt lakás',  # Jelmagyarázat szövege.
        )
        # Ugyanígy rajzolunk egy vonalat az 'Új lakás' adatok alapján.
        plt.plot(
            self.data['Év'],  # Az x-tengelyre kerülő értékek (évek).
            self.data['Új lakás'],  # Az y-tengelyre kerülő értékek (új lakások száma).
            label='Új lakás',  # Jelmagyarázat szövege.
        )
        
        # Beállítjuk az y-tengely lépésközeit 20000-es intervallumokra.
        plt.yticks(np.arange(0, self.max_y_value + 20000, 20000))

        # Az x-tengely értékeihez beállítjuk, hogy az évek megfelelően olvashatóak legyenek.
        plt.xticks(
            self.data['Év'],  # Az x-tengelyen megjelenő értékek.
            rotation=45  # Az értékek 45 fokos elforgatása az olvashatóság érdekében.
        )
        
        plt.xlabel('Év') # Az x-tengely címkéjét állítjuk be.
        plt.ylabel('Lakások száma') # Az y-tengely címkéjét állítjuk be.
        plt.title('Használt és új lakások eladásának száma évenként') # Beállítjuk a diagram címét.
        plt.legend() # Megjelenítjük a jelmagyarázatot.
        plt.grid(True) # Rácsvonalakat jelenítünk meg a diagramon.

   # Egy új metódus előkészítése, amely hisztogramot fog készíteni.
    def scatter_plot(self):
        # Pontdiagram elhelyezése a lap alján.
        plt.subplot(2, 1, 2)

        # Kirajzoljuk a 'Használt lakás' pontjait.
        plt.scatter(
            self.data['Év'], # Az x-tengelyre kerülő értékek (évek).
            self.data['Használt lakás'], # Az y-tengelyre kerülő értékek (használt lakások száma).
            label='Használt lakás', # Jelmagyarázat szövege.
            marker='o' # Az adatok pontjainál kör alakú jelölést használunk.
        )

        # Kirajzoljuk az 'Új lakás' pontjait.
        plt.scatter(
            self.data['Év'], # Az x-tengelyre kerülő értékek (évek).
            self.data['Új lakás'], # Az y-tengelyre kerülő értékek (új lakások száma).
            label='Új lakás', # Jelmagyarázat szövege.
            marker='o' # Az adatok pontjainál kör alakú jelölést használunk.
        )

        # Beállítjuk az y-tengely maximáélis értékét és lépésközeit 20000-es intervallumokra.
        plt.yticks(np.arange(0, self.max_y_value + 20000, 20000))

        # Az x-tengely értékeihez beállítjuk, hogy az évek megfelelően olvashatóak legyenek.
        plt.xticks(
            self.data['Év'],  # Az x-tengelyen megjelenő értékek.
            rotation=45  # Az értékek 45 fokos elforgatása az olvashatóság érdekében.
        )

        regUsed = LinearRegression().fit(self.data['Év'].values.reshape(-1,1),self.data['Használt lakás'].values)
        yUsed_predict = regUsed.predict(self.data['Év'].values.reshape(-1,1))
        plt.plot(self.data['Év'],yUsed_predict,label='Használt lakás trend',linestyle = '--')

        regNew = LinearRegression().fit(self.data['Év'].values.reshape(-1,1),self.data['Új lakás'].values)
        yNew_predict = regNew.predict(self.data['Év'].values.reshape(-1,1))
        plt.plot(self.data['Év'],yNew_predict,label='Új lakás trend',linestyle = '--')

        plt.xlabel('Év')  # Az x-tengely címkéjét állítjuk be.
        plt.ylabel('Lakások száma')  # Az y-tengely címkéjét állítjuk be.
        plt.title('Pontdiagram')  # Beállítjuk a diagram címét.
        plt.legend()  # Megjelenítjük a jelmagyarázatot.
        plt.tight_layout()  # A diagram elemeinek elrendezését optimalizáljuk, hogy ne fedjék egymást.
        plt.show()  # Megjelenítjük a diagramot.
