from uzorak import Uzorak
from scipy.stats import linregress
import numpy as np

class Test:
    def __init__(self, redni_broj: int, time: list[float], force: list[float], streak: list[float], extension: list[float], uzorak: Uzorak, udaljenost_celjusti: float, granica_linearnosti: int):
        self.redni_broj = redni_broj
        self.time = time
        self.force = force
        self.streak = streak
        self.extension = extension
        self.uzorak = uzorak
        self.udaljenost_celjusti = udaljenost_celjusti
        self.granica_linearnosti = granica_linearnosti
        
        self.area = self.uzorak.povrsina
        self.stress: list[float] = []
        self.strain: list[float] = []

        for current_force in self.force:
            tmp = current_force / self.area
            self.stress.append(tmp)

        for current_extension in self.extension:
            tmp = current_extension / self.udaljenost_celjusti
            self.strain.append(tmp)

        self.stress_elasticity = np.array(self.stress[:self.granica_linearnosti])
        self.strain_elasticity = np.array(self.strain[:self.granica_linearnosti])

        self.vlacna_cvrstoca = np.max(self.stress)
        self.pocetna_visina_uzorka = self.uzorak.visina * 10
        self.zavrsna_ekstenzija = self.extension[-1]
        self.zavrsna_visina_uzorka = self.pocetna_visina_uzorka + self.zavrsna_ekstenzija
        self.postotak_ekstenzije = (self.zavrsna_ekstenzija / self.pocetna_visina_uzorka) * 100

        try:
            self.slope, _, _, _, _ = linregress(self.strain_elasticity, self.stress_elasticity)
        except:
            self.slope = 544

        self.modulus = self.slope * 1e6