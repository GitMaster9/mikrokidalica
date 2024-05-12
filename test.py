from uzorak import Uzorak
from scipy.stats import linregress
import numpy as np

class Test:
    def __init__(self, time: list[float], force: list[float], streak: list[float], extension: list[float], uzorak: Uzorak, udaljenost_celjusti: float, granica_linearnosti: int):
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

        try:
            self.slope, _, _, _, _ = linregress(self.strain_elasticity, self.stress_elasticity)
        except:
            self.slope = 544

        self.modulus = self.slope * 1e6