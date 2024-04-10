import numpy as np #se importa la biblioteca numpy y le asigna el alias np

import matplotlib.pyplot as plt #importa la biblioteca matplotlib y asigna el alias plt


def mandelbrot(h, w, maxit=20, r=2): #Crea una funcion con tres argumentod, en donde maxit y r son argumentos predeterminados, lista de matrices con la funcion de dar coordenas a partir de los vectores
    x = np.linspace(-2.5, 1.5, 4*h+1) #lista de elementos equiespaciodos que empieza por -2.5 hasta 1.5 en donde entre esos numeros se generan espaciados de (4*h+1)
    y = np.linspace(-1.5, 1.5, 3*w+1) #lista de elementos equiespaciodos que empieza por -1.5 hasta 1.5 en donde entre esos numeros se generan espaciados de (4*w+1)
    A, B = np.meshgrid(x, y) #asignacion multiple por medio de una funcion que asigna a A la matriz x y a B la matriz y
    C = A + B*1j #da el valor de la varible c por medio de la suma entre a y B multiplicado por un numero complejo
    z = np.zeros_like(C) #Crea una matriz de ceros con la forma de la varible c
    divtime = maxit + np.zeros(z.shape, dtype=int) #se suma la variable maxit con el arreglo de ceros con la  

    for i in range(maxit): #for que recorre en el rango de maxit osea 20
        z = z**2 + C                            # z toma su valor y se eleva al cuadrado y se suma c
        diverge = abs(z) > r                    # 
        div_now = diverge & (divtime == maxit)  # who is diverging now
        divtime[div_now] = i                    # note when
        z[diverge] = r                          # avoid diverging too much

    return divtime
plt.clf()
plt.imshow(mandelbrot(400, 400))