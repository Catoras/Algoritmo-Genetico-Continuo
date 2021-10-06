class Quartic:
    MIN_VALUE = -5.12
    MAX_VALUE = 5.12
    def __init__(self):
        pass
    def fitness(self, cromosoma):
        z = 0
        for i in range(0,len(cromosoma)):
            z += (i+1) * ((cromosoma[i])**4)
        return z
