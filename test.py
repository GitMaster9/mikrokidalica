from uzorak import Uzorak

class Test:
    def __init__(self, time: list[float], force: list[float], streak: list[float], extension: list[float], uzorak: Uzorak, udaljenost_celjusti: float):
        self.time = time
        self.force = force
        self.streak = streak
        self.extension = extension
        self.uzorak = uzorak
        self.udaljenost_celjusti = udaljenost_celjusti
        
        self.area = self.uzorak.povrsina
        self.stress: list[float] = []
        self.strain: list[float] = []

        for current_force in self.force:
            tmp = current_force / self.area
            self.stress.append(tmp)

        for current_extension in self.extension:
            tmp = current_extension / self.udaljenost_celjusti
            self.strain.append(tmp)