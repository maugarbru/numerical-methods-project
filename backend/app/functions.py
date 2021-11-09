import numpy as np

def simpson(a, b, n, funcion):
    h = (b - a) / n
    puntos = np.linspace(a , b, n + 1, endpoint=True)
    print(puntos)
    fx0 = eval(funcion, {'x': a})
    fxn = eval(funcion, {'x': b})
    suma_par = 0
    suma_impar = 0
    for i in range(1, n):
        if (i%2 == 0):
            suma_par = suma_par + eval(funcion, {'x': puntos[i]})
        elif (i%2 != 0):
            suma_impar =  suma_impar + eval(funcion, {'x': puntos[i]})
    return (h) * ((fx0 + 4 * suma_impar + 2 * suma_par + fxn) / (3))

def centradas(x, delta, f):
    return (eval(f, {'x': x + (delta / 2)}) - (eval(f, {'x': x - (delta / 2)})))/delta