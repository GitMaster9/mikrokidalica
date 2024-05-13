from pathlib import Path
import pandas
import numpy as np
import matplotlib.pyplot as plt

from uzorak import Uzorak
from test import Test

class Tester:
    def __init__(self, folder: Path, udaljenost_celjusti: float, granica_linearnosti: int):
        self.folder = folder
        self.udaljenost_celjusti = udaljenost_celjusti
        self.granica_linearnosti = granica_linearnosti
        
        path = self.folder / "dimenzije.xlsx"
        df = pandas.read_excel(path)

        sirina = df.iloc[:, 1].to_list()
        debljina = df.iloc[:, 2].to_list()
        visina = df.iloc[:, 3].to_list()
        
        self.testovi: list[Test] = []
        for i in range(6):
            path = folder / f"{i + 1}.csv"

            df = pandas.read_csv(path, skiprows=2)
            df = df.apply(lambda x: safe_float_conversion(x) if x.dtype == 'object' else x)

            time_list = df.iloc[:, 0].to_list()
            force_list = df.iloc[:, 1].to_list()
            stroke_list = df.iloc[:, 2].to_list()
            extension_list = df.iloc[:, 3].to_list()

            uzorak = Uzorak(i + 1, sirina[i], debljina[i], visina[i])

            tmp = Test(i + 1, time_list, force_list, stroke_list, extension_list, uzorak, self.udaljenost_celjusti, self.granica_linearnosti)
            self.testovi.append(tmp)

        self.cvrstoce = []
        self.elasticnosti = []

        for test in self.testovi:
            self.cvrstoce.append(test.vlacna_cvrstoca)
            self.elasticnosti.append(test.modulus)

        self.prosjecna_cvrstoca = np.average(self.cvrstoce)
        self.prosjecna_elasticnost = np.average(self.elasticnosti)

        self.standardna_devijacija_cvrstoca = np.std(self.cvrstoce)
        self.standardna_devijacija_elasticnost = np.std(self.elasticnosti)

    def __str__(self):
        output = "ANALIZA TESTIRANJA\n"

        output += f"Udaljenost čeljusti: {self.udaljenost_celjusti} mm\n"
        output += f"Broj točaka za izračun modula elastičnosti: {self.granica_linearnosti}\n"

        output += "\n"

        for test in self.testovi:
            output += f"TEST {test.redni_broj}\n"
            output += f"Vlačna čvrstoća: {round(test.vlacna_cvrstoca, 3)} N/mm2\n"
            output += f"Modul elastičnosti: {test.modulus:.3e} Pa\n"

        output += "\n"

        output += f"Prosječna vlačna čvrstoća: {round(self.prosjecna_cvrstoca, 3)} N/mm2\n"
        output += f"Standardna devijacija vlačne čvrstoće: {round(self.standardna_devijacija_cvrstoca, 3)} N/mm2\n"
        
        output += "\n"

        output += f"Prosječni modul elastičnosti: {self.prosjecna_elasticnost:.3e} Pa\n"
        output += f"Standardna devijacija modula elastičnosti: {self.standardna_devijacija_elasticnost:.3e} Pa\n" 

        return output
    
    def graf_testa(self, redni_broj: int):
        if redni_broj <= 0:
                print(f"Netočan redni broj: {redni_broj}. Redni brojevi su od 1 do 6")
                return
        
        try:
            test = self.testovi[redni_broj - 1]
        except:
            print(f"Test pod rednim brojem {redni_broj} ne postoji")
            return
        
        plt.figure()

        plt.plot(test.strain, test.stress)
        plt.xlabel('Strain [%]')
        plt.ylabel('Stress [N/mm2]')
        plt.title('Stress-Strain dijagram')
        plt.axvline(x=test.strain_elasticity[-1], color='r', linestyle='--')
        plt.show()
    
    def boxplot_cvrstoca(self):
        plt.figure()
        plt.boxplot(self.cvrstoce, patch_artist=True)

        plt.title('Kutijasti dijagram - vlačna čvrstoća')
        plt.ylabel('Vlačna čvrstoća [N/mm2]')

        plt.show()

    def boxplot_elasticnost(self):
        plt.figure()
        plt.boxplot(self.elasticnosti, patch_artist=True)

        plt.title('Kutijasti dijagram - modul elastičnosti')
        plt.ylabel('Modul elastičnosti [Pa]')

        plt.show()

def safe_float_conversion(value):
    try:
        return value.str.replace(',', '.').astype(float)
    except ValueError:
        return -69.69