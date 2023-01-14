class Stadion:
    def __init__(self, sor):
        self.stadion_nev = sor[0]
        self.varos = sor[1]
        self.csapatszam = int(sor[2])
        self.elso = sor[3]
        self.utolso = sor[4]


    def __str__(self):
        return f"{self.stadion_nev}, {self.varos}, {self.csapatszam}, {self.elso}, {self.utolso}"