class Uzorak:
    def __init__(self, redni_broj: int, sirina: float, debljina: float, visina: float):
        self.redni_broj = redni_broj
        self.sirina = sirina
        self.debljina = debljina
        self.visina = visina

        self.povrsina = self.sirina * self.debljina