import math

class Rastrigin:
    MIN_VALUE = -5.12
    MAX_VALUE = 5.12
    def __init__(self):
        pass
    def fitness(self, cromosoma):
        z = 0
        for i in range(0,len(cromosoma)):
            z += ((cromosoma[i])**2)-(10 * (math.cos((2*math.pi*cromosoma[i]))))
        return (10*len(cromosoma))+z
