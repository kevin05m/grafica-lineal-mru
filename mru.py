#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np

class MRU:
    def __init__(self, vel1, vel2, sepinicial):
        self.vel1 = vel1
        self.vel2 = vel2
        self.sepinicial = sepinicial

    def run(self):
        x = np.linspace(0, 40, 100)
        
        y1 = self.vel1 * x
        y2 = self.vel2 * x + self.sepinicial
        
        punto_interseccion_x = self.sepinicial / (self.vel1 - self.vel2)
        punto_interseccion_y = self.vel1 * punto_interseccion_x
        
        plt.plot(x, y1, label=f'Función 1: {self.vel1}m/s')
        plt.plot(x, y2, label=f'Función 2: {self.vel2}m/s')
        
        plt.plot(punto_interseccion_x, punto_interseccion_y, 'ro', label=f'Punto de Intersección:\nTiempo: {punto_interseccion_x}\nDistacia: {punto_interseccion_y}')
        
        plt.grid(True)
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Distancia (m)')
        plt.title('Grafica Lineal de MRU (alcance y encuentro)')
        plt.legend()
        plt.show()

def main():
    vel1 = float(input("Ingrese la velocidad del primer carrito (m/s): "))  # m/s
    vel2 = float(input("Ingrese la velocidad del segundo carrito (m/s): "))  # m/s
    sepinicial = float(input("Ingrese la separacion de los carritos (m): "))  # metros
    mru = MRU(vel1, vel2, sepinicial)
    mru.run()

if __name__ == '__main__':
    main()
