from pathlib import Path
import pandas
from uzorak import Uzorak

from test import Test

class Tester:
    def __init__(self, folder: Path, udaljenost_celjusti: float):
        self.udaljenost_celjusti = udaljenost_celjusti
        
        path = folder / "dimenzije.xlsx"
        df = pandas.read_excel(path)

        sirina = df.iloc[:, 1].to_list()
        debljina = df.iloc[:, 2].to_list()
        visina = df.iloc[:, 3].to_list()
        
        self.testovi: list[Test] = []
        for i in range(6):
            path = folder / f"{i + 1}.csv"

            df = pandas.read_csv(path, skiprows=2)
            df = df.apply(lambda x: x.str.replace(',', '.').astype(float) if x.dtype == 'object' else x)

            time_list = df.iloc[:, 0].to_list()
            force_list = df.iloc[:, 1].to_list()
            stroke_list = df.iloc[:, 2].to_list()
            extension_list = df.iloc[:, 3].to_list()

            uzorak = Uzorak(i + 1, sirina[i], debljina[i], visina[i])

            tmp = Test(time_list, force_list, stroke_list, extension_list, uzorak, self.udaljenost_celjusti)
            self.testovi.append(tmp)