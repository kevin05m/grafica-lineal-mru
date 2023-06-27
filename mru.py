#!/usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk

class MRU:
    def __init__(self, vel1, vel2, sepinicial):
        self.vel1 = vel1
        self.vel2 = vel2
        self.sepinicial = sepinicial

    def DibujarMru(self):
        x = np.linspace(0, 100, 100)
        
        y1 = self.vel1 * x
        y2 = self.vel2 * x + self.sepinicial
        
        punto_interseccion_x = self.sepinicial / (self.vel1 - self.vel2)
        punto_interseccion_y = self.vel1 * punto_interseccion_x
        
        plt.plot(x, y1, label=f'Función 1: {self.vel1}m/s')
        plt.plot(x, y2, label=f'Función 2: {self.vel2}m/s')
        
        plt.plot(punto_interseccion_x, punto_interseccion_y, 'ro', label=f'Punto de Intersección:\nTiempo: {punto_interseccion_x} s\nDistacia: {punto_interseccion_y} m')
        
        plt.grid(True)
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Distancia (m)')
        plt.title('Grafica Lineal de MRU (alcance y encuentro)')
        plt.legend()
        plt.show() 

def graficar_funcion():
    vel1 = float(entry_velocidad1.get())
    vel2 = float(entry_velocidad2.get())
    sepinicial = float(entry_separacion.get())
    mru = MRU(vel1, vel2, sepinicial)
    mru.DibujarMru()

ventana = tk.Tk()
ventana.title('Graficar funciones lineales')
label_velocidad1 = tk.Label(ventana, text='Velocidad 1 (m/s):')
label_velocidad1.pack()
entry_velocidad1 = tk.Entry(ventana)
entry_velocidad1.pack()
label_velocidad2 = tk.Label(ventana, text='Velocidad 2 (m/s):')
label_velocidad2.pack()
entry_velocidad2 = tk.Entry(ventana)
entry_velocidad2.pack()
label_separacion = tk.Label(ventana, text='Separación inicial (metros):')
label_separacion.pack()
entry_separacion = tk.Entry(ventana)
entry_separacion.pack()
boton_graficar = tk.Button(ventana, text='Graficar', command=graficar_funcion)
boton_graficar.pack()
ventana.mainloop()