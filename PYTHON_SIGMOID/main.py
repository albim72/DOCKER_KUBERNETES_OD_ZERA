import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

if __name__ == '__main__':
    x = float(input("podaj wartosc argumentu x funkcji sigmoid: "))
    print(f"wartośc funkcji sigmoid dla x = {x} wynosi {sigmoid(x):.8f}")
