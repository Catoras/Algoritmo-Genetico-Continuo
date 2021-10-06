import sphere
import rosenbrock
import rastrigin
import quartic
import AGC

def main():
    #f = sphere.Sphere()
    #f = rosenbrock.Rosenbrock()
    #f = rastrigin.Rastrigin()
    f = quartic.Quartic()
    ag = AGC.AGC(128, 8 , 2000, 0.02, f, False)
    ag.run()

if __name__ == '__main__':
    main()
