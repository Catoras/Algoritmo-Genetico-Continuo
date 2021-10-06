class Rosenbrock:
    MIN_VALUE = -5.12
    MAX_VALUE = 5.12
    def __init__(self):
        pass
    def fitness(self, cromosoma):
        z = 0
        for i in range(0,len(cromosoma)-1):
            z += (100 * (((cromosoma[i+1])-((cromosoma[i])**2))**2)) + (((cromosoma[i])-1)**2)
        return z
