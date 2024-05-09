# Importa la librería tkinter y la renombra como tk
import tkinter as tk
# Importa todas las clases y funciones de la librería tkinter
from tkinter import *
# Importa la clase messagebox de la librería tkinter para mostrar mensajes de alerta
from tkinter import messagebox
# Importa la clase Tooltip del módulo Tooltip para mostrar información adicional sobre los botones
from Tooltip import Tooltip
# Importa el módulo pygame.mixer y lo renombra como mx para reproducir archivos de audio
import pygame.mixer as mx

# Define una clase llamada Reproductor para crear una aplicación reproductora de música
class Reproductor():
    # Método para reproducir la pista de audio
    def play(self, event):
        # Carga la pista de audio utilizando pygame.mixer
        mx.music.load(r"sounds\Pista.mp3")
        # Reproduce la pista de audio
        mx.music.play()
        # Actualiza el estado de reproducción
        self.lblEstado.config(text="Reproduciendo...")
        # Habilita el botón de pausa y detener, y deshabilita el botón de reproducción
        self.btnPause.config(state="normal")
        self.btnStop.config(state="normal")
        self.btnPlay.config(state="disabled")

    # Método para pausar o reanudar la reproducción de la pista de audio
    def pause(self, event):
        # Verifica el estado de reproducción actual
        if(self.bandera == False):
            # Si la reproducción no está pausada, pausa la reproducción
            mx.music.pause()
            # Actualiza el estado de reproducción
            self.lblEstado.config(text="Reproducción Pausada...")
            # Habilita el botón de pausa y detener, y deshabilita el botón de reproducción
            self.btnPause.config(state="normal")
            self.btnStop.config(state="normal")
            self.btnPlay.config(state="disabled")
            self.bandera = True
        else:
            # Si la reproducción está pausada, reanuda la reproducción
            mx.music.unpause()
            # Actualiza el estado de reproducción
            self.lblEstado.config(text="Reproduciendo...")
            # Habilita el botón de pausa y detener, y deshabilita el botón de reproducción
            self.btnPause.config(state="normal")
            self.btnStop.config(state="normal")
            self.btnPlay.config(state="disabled")
            self.bandera = False

    # Método para detener la reproducción de la pista de audio
    def stop(self, event):
        # Detiene la reproducción de la pista de audio
        mx.music.stop()
        # Actualiza el estado de reproducción
        self.lblEstado.config(text="Reproducción Detenida...")
        # Deshabilita el botón de pausa y detener, y habilita el botón de reproducción
        self.btnPause.config(state="disabled")
        self.btnStop.config(state="disabled")
        self.btnPlay.config(state="normal")

    # Método constructor de la clase
    def __init__(self):
        # Crea una nueva ventana de tkinter
        self.ventana = tk.Tk()
        # Establece el título de la ventana
        self.ventana.title("Mi Reproductor")
        # Configura el tamaño de la ventana
        self.ventana.config(width=500, height=500)
        # Evita que la ventana pueda redimensionarse
        self.ventana.resizable(0,0)

        # Inicializa pygame.mixer para reproducir audio
        mx.init()
        # Inicializa la bandera para controlar el estado de reproducción
        self.bandera = False

        # Carga los iconos de los botones de reproducción
        iconoPlay = tk.PhotoImage(file=r"icons\control_play.png")
        iconoPause = tk.PhotoImage(file=r"icons\control_pause.png")
        iconoStop = tk.PhotoImage(file=r"icons\control_stop.png")

        # Crea el botón de reproducción
        self.btnPlay = tk.Button(self.ventana, image=iconoPlay)
        self.btnPlay.place(relx=0.5, rely=1, y=-50, width=25, height=25)
        # Asocia el método play al evento de clic del botón de reproducción
        self.btnPlay.bind("<Button-1>", self.play)
        # Crea un mensaje emergente de información para el botón de reproducción
        Tooltip(self.btnPlay, "Presione para Iniciar la reproducción...")

        # Crea el botón de pausa y lo deshabilita inicialmente
        self.btnPause = tk.Button(self.ventana, image=iconoPause, state="disabled")
        self.btnPause.place(relx=0.5, rely=1, y=-50, x=50, width=25, height=25)
        # Asocia el método pause al evento de clic del botón de pausa
        self.btnPause.bind("<Button-1>", self.pause)
        # Crea un mensaje emergente de información para el botón de pausa
        Tooltip(self.btnPause, "Presione para Pausar la reproducción...")

        # Crea el botón de detener y lo

 deshabilita inicialmente
        self.btnStop = tk.Button(self.ventana, image=iconoStop, state="disabled")
        self.btnStop.place(relx=0.5, rely=1, y=-50, x=-50, width=25, height=25)
        # Asocia el método stop al evento de clic del botón de detener
        self.btnStop.bind("<Button-1>", self.stop)
        # Crea un mensaje emergente de información para el botón de detener
        Tooltip(self.btnStop, "Presione para Detener la reproducción...")

        # Crea una etiqueta para mostrar el estado de reproducción
        self.lblEstado = tk.Label(self.ventana, text="Cargando...")
        self.lblEstado.place(relx=0.5, rely=0.5, anchor="center")

        # Inicia el bucle principal de la aplicación
        self.ventana.mainloop()