import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from Tooltip import Tooltip
import pygame.mixer as mx
import pygame
import os
import mutagen
from mutagen.mp3 import MP3

class Reproductor():
    pygame.mixer.init()
    pygame.mixer.init(frequency=44100)
    cancionActual = ""
    direccion = ""
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Reproductor de Musica")
        self.ventana.config(width=700, height=500)
        self.ventana.resizable(0,0)

        self.pantalla = Listbox(self.ventana, bg="lightblue", fg="blue", width=60, selectbackground="white", selectforeground="black")
        self.pantalla.place(rely=20)

        lista_canciones = tk.Listbox(self.ventana, width=300, height=200)
        lista_canciones.place(x=10, y=10)

        self.directorio = []
        self.posicion = 0
        self.cancionActual = None


        mx.init()
        self.bandera = False

        iconoPlay = tk.PhotoImage(file=r"laboratorio\icons\control_play.png")
        iconoPause = tk.PhotoImage(file=r"laboratorio\icons\control_pause.png")
        iconoStop = tk.PhotoImage(file=r"laboratorio\icons\control_stop.png")
        iconoAnterior = tk.PhotoImage(file=r"laboratorio\icons\control_start.png")
        iconoSiguiente = tk.PhotoImage(file=r"laboratorio\icons\control_end.png")

        self.btnPlay = tk.Button(self.ventana, image=iconoPlay)
        self.btnPlay.place(relx=0.5, rely=1, y=-50, width=25, height=25)
        self.btnPlay.bind("<Button-1>", self.play)
        Tooltip(self.btnPlay, "Presione para Iniciar la reproducción...")

        self.btnPause = tk.Button(self.ventana, image=iconoPause, state="disabled")
        self.btnPause.place(relx=0.5, rely=1, y=-50, x=50, width=25, height=25)
        self.btnPause.bind("<Button-1>", self.pause)
        Tooltip(self.btnPause, "Presione para Pausar la reproducción...")

        self.btnStop = tk.Button(self.ventana, image=iconoStop, state="disabled")
        self.btnStop.place(relx=0.5, rely=1, y=-50, x=-50, width=25, height=25)
        self.btnStop.bind("<Button-1>", self.stop)
        Tooltip(self.btnStop, "Presione para Detener la reproducción...")

        self.btnAnterior = tk.Button(self.ventana, image=iconoAnterior)
        self.btnAnterior.place(relx=0.5, rely=1, y=-50, x=-90, width=25, height=25)
        self.btnAnterior.bind("<Button-1>", self.anterior)
        Tooltip(self.btnAnterior, "Presione para reproducir la cancion anterior...")

        self.btnSiguiente = tk.Button(self.ventana, image=iconoSiguiente)
        self.btnSiguiente.place(relx=0.5, rely=1, y=-50, x=90, width=25, height=25)
        self.btnSiguiente.bind("<Button-1>", self.anterior)
        Tooltip(self.btnSiguiente, "Presione para reproducir la cancion anterior...")

        self.lblEstado = tk.Label(self.ventana, text="Cargando...")
        self.lblEstado.place(relx=0.5, rely=0.5, anchor="center")

    
    def abrirArchivo(self):
        self.directorio = filedialog.askopenfilenames(initialdir='/',
                                                title='Elegir la cancion',
                                                filetypes=(('mp3 files', '*.mp3*'), ('All files', '*.*')))
        self.posicion = 0
        self.num = len(self.directorio)
        self.cancionActual = self.directorio[self.posicion]
        self.nombreCancion = self.cancionActual.split('/')[-1]
    
    lista = []
    for i in range(50,200,10):
        lista.append(i)
    

    def play(self, event):
        self.canciones_seleccionadas = self.pantalla.get(ACTIVE)  # Get selected song
        if self.canciones_seleccionadas:  # Check if a song is selected
            ruta_archivo = os.path.join(r"C:\Users\User\Desktop\LABORATORIO-1\laboratorio\music", self.cancion)
            try:
                pygame.mixer.music.load(ruta_archivo)
                pygame.mixer.music.play(loops=0)
            except pygame.error:
                print(f"Error: No se pudo cargar el archivo {ruta_archivo}")
        else:
            print("Selecciona una canción para reproducir")

        self.lblEstado.config(text="Reproduciendo...")
        self.btnPause.config(state="normal")
        self.btnStop.config(state="normal")
        self.btnPlay.config(state="disabled")

    def stop(self, event):
        mx.music.stop()
        self.pantalla.selection_clear(ACTIVE)
        mx.music.stop()
        self.lblEstado.config(text="Reproducción Detenida...")
        self.btnPause.config(state="disabled")
        self.btnStop.config(state="disabled")
        self.btnPlay.config(state="normal")

    def siguiente(self, event):
        self.proxima = self.pantalla.curselection()
        self.proxima = self.proxima[0]+1
        self.cancion = self.pantalla.get(self.proxima)
        self.cancion = f"{self.cancion}.mp3"

        mx.music.load(self.cancion)
        mx.music.play(loops=0)

        self.pantalla.selection_clear(0, END)
        self.pantalla.activate(self.proxima)
        LAST = None
        self.pantalla.selection_set(self.proxima, LAST)

    def anterior(self,event):
        self.proxima = self.pantalla.curselection()
        self.proxima = self.proxima[0]-1
        self.cancion = self.pantalla.get(self.proxima)
        self.cancion = f"{self.cancion}.mp3"

        mx.music.load(self.cancion)
        mx.music.play(loops=0)

        self.pantalla.selection_clear(0,END)
        self.pantalla.activate(self.proxima)

        LAST = None
        self.pantalla.selection_set(self.proxima, LAST)

    def pause(self, event):
        if(self.bandera == False):
            mx.music.pause()
            self.lblEstado.config(text="Reproducción Pausada...")
            self.btnPause.config(state="normal")
            self.btnStop.config(state="normal")
            self.btnPlay.config(state="disabled")
            self.bandera = True
        else:
            mx.music.unpause()
            self.lblEstado.config(text="Reproduciendo...")
            self.btnPause.config(state="normal")
            self.btnStop.config(state="normal")
            self.btnPlay.config(state="disabled")
            self.bandera = False
    
    def borrar(self, event):
        self.pantalla.delete(ANCHOR)

        mx.music.stop()

    def borrarTodas(self, event):
        self.pantalla.delete(0,END)

        mx.music.stop()

    

        self.ventana.mainloop()