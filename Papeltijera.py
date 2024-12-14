import tkinter as tk
from tkinter import messagebox
import random
import time

class JuegoPiedraPapelTijera:
    def __init__(self):
        # Inicialización de puntuaciones
        self.puntaje_jugador = 0
        self.puntaje_computadora = 0
        self.racha_jugador = 0

        # Crear la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Piedra, Papel o Tijera")
        self.ventana.geometry("700x700")
        self.ventana.config(bg="#2F4F4F")  # Fondo oscuro

        # Título
        self.titulo = tk.Label(self.ventana, text="¡Piedra, Papel o Tijera!", font=("Arial", 26, "bold"), fg="#F5F5F5", bg="#2F4F4F")
        self.titulo.pack(pady=30)

        # Etiquetas para mostrar los resultados
        self.resultado_label = tk.Label(self.ventana, text="Selecciona una opción", font=("Arial", 18), fg="#F5F5F5", bg="#2F4F4F")
        self.resultado_label.pack(pady=10)

        self.seleccion_computadora_label = tk.Label(self.ventana, text="Computadora elige...", font=("Arial", 16), fg="#F5F5F5", bg="#2F4F4F")
        self.seleccion_computadora_label.pack(pady=10)

        self.puntaje_label = tk.Label(self.ventana, text=f"Puntaje - Jugador: {self.puntaje_jugador}  Computadora: {self.puntaje_computadora}", font=("Arial", 16), fg="#F5F5F5", bg="#2F4F4F")
        self.puntaje_label.pack(pady=20)

        self.racha_label = tk.Label(self.ventana, text=f"Racha: {self.racha_jugador} victorias", font=("Arial", 14), fg="#F5F5F5", bg="#2F4F4F")
        self.racha_label.pack(pady=10)

        # Frame para los botones
        self.boton_frame = tk.Frame(self.ventana, bg="#2F4F4F")
        self.boton_frame.pack(pady=40)

        # Botones con estilo para seleccionar Piedra, Papel o Tijera
        self.boton_piedra = self.crear_boton("Piedra", "#FF6347", lambda: self.jugar("Piedra"))
        self.boton_piedra.grid(row=0, column=0, padx=30)

        self.boton_papel = self.crear_boton("Papel", "#1E90FF", lambda: self.jugar("Papel"))
        self.boton_papel.grid(row=0, column=1, padx=30)

        self.boton_tijera = self.crear_boton("Tijera", "#32CD32", lambda: self.jugar("Tijera"))
        self.boton_tijera.grid(row=0, column=2, padx=30)

        # Añadir imagen a las opciones
        self.img_piedra = tk.PhotoImage(file="piedra.png")  # Asegúrate de tener esta imagen
        self.img_papel = tk.PhotoImage(file="papel.png")    # Asegúrate de tener esta imagen
        self.img_tijera = tk.PhotoImage(file="tijera.png")  # Asegúrate de tener esta imagen
        self.img_ganaste = tk.PhotoImage(file="ganaste.png")  # Asegúrate de tener este ícono
        self.img_perdiste = tk.PhotoImage(file="perdiste.png")  # Asegúrate de tener este ícono
        self.img_empate = tk.PhotoImage(file="empate.png")  # Asegúrate de tener este ícono

        # Etiqueta para mostrar la imagen seleccionada por la computadora
        self.imagen_computadora_label = tk.Label(self.ventana, image=self.img_piedra, bg="#2F4F4F")
        self.imagen_computadora_label.pack(pady=10)

        # Botón para reiniciar el juego
        self.boton_reiniciar = tk.Button(self.ventana, text="Reiniciar Juego", font=("Arial", 14, "bold"), bg="#FF4500", fg="#fff", command=self.reiniciar)
        self.boton_reiniciar.pack(pady=20)

        # Fondo adicional para un toque más visual
        self.fondo_frame = tk.Frame(self.ventana, bg="#2F4F4F")
        self.fondo_frame.pack(fill="both", expand=True)

    def crear_boton(self, texto, color, comando):
        """Crea un botón estilizado con efecto hover y bordes redondeados"""
        boton = tk.Button(self.boton_frame, text=texto, command=comando, width=12, height=3, font=("Arial", 14, "bold"), bg=color, fg="#fff", relief="flat", bd=0, highlightthickness=0)
        boton.config(activebackground="#ffcc00", activeforeground="black", fg="#fff")
        boton.bind("<Enter>", lambda e: boton.config(bg="#ffcc00", fg="black", relief="solid", bd=2))  # Cambio de color al pasar el ratón
        boton.bind("<Leave>", lambda e: boton.config(bg=color, fg="#fff", relief="flat", bd=0))  # Restaurar color al quitar el ratón
        boton.config(borderwidth=2, relief="raised", padx=10, pady=10)
        return boton

    def obtener_eleccion_computadora(self):
        """Devuelve una elección aleatoria de la computadora"""
        opciones = ["Piedra", "Papel", "Tijera"]
        return random.choice(opciones)

    def obtener_resultado(self, eleccion_jugador, eleccion_computadora):
        """Determina el resultado del juego"""
        if eleccion_jugador == eleccion_computadora:
            return "Empate"
        elif (eleccion_jugador == "Piedra" and eleccion_computadora == "Tijera") or \
             (eleccion_jugador == "Tijera" and eleccion_computadora == "Papel") or \
             (eleccion_jugador == "Papel" and eleccion_computadora == "Piedra"):
            return "Ganaste"
        else:
            return "Perdiste"

    def actualizar_puntuaciones(self, resultado):
        """Actualiza las puntuaciones del jugador y la computadora"""
        if resultado == "Ganaste":
            self.puntaje_jugador += 1
            self.racha_jugador += 1
        elif resultado == "Perdiste":
            self.puntaje_computadora += 1
            self.racha_jugador = 0
        # Actualizar la etiqueta de puntajes
        self.puntaje_label.config(text=f"Puntaje - Jugador: {self.puntaje_jugador}  Computadora: {self.puntaje_computadora}")
        self.racha_label.config(text=f"Racha: {self.racha_jugador} victorias")

    def actualizar_imagen_computadora(self, eleccion_computadora):
        """Actualiza la imagen que muestra la elección de la computadora"""
        if eleccion_computadora == "Piedra":
            self.imagen_computadora_label.config(image=self.img_piedra)
        elif eleccion_computadora == "Papel":
            self.imagen_computadora_label.config(image=self.img_papel)
        elif eleccion_computadora == "Tijera":
            self.imagen_computadora_label.config(image=self.img_tijera)

    def mostrar_resultado_icono(self, resultado):
        """Muestra un icono correspondiente al resultado"""
        if resultado == "Ganaste":
            self.resultado_label.config(text="¡Ganaste!")
            self.resultado_label.config(fg="#32CD32")
            self.imagen_computadora_label.config(image=self.img_ganaste)
        elif resultado == "Perdiste":
            self.resultado_label.config(text="Perdiste!")
            self.resultado_label.config(fg="#FF6347")
            self.imagen_computadora_label.config(image=self.img_perdiste)
        elif resultado == "Empate":
            self.resultado_label.config(text="Empate!")
            self.resultado_label.config(fg="#FFD700")
            self.imagen_computadora_label.config(image=self.img_empate)

    def jugar(self, eleccion_jugador):
        """Función que maneja la lógica del juego"""
        # Elección de la computadora
        eleccion_computadora = self.obtener_eleccion_computadora()

        # Pausa de 1 segundo para simular la espera de la computadora
        self.seleccion_computadora_label.config(text="Computadora eligiendo...")
        self.ventana.update()
        time.sleep(1)

        # Obtener el resultado
        resultado = self.obtener_resultado(eleccion_jugador, eleccion_computadora)

        # Actualizar puntuaciones
        self.actualizar_puntuaciones(resultado)

        # Mostrar los resultados en la interfaz
        self.seleccion_computadora_label.config(text=f"Computadora eligió: {eleccion_computadora}")
        
        # Mostrar resultado visual
        self.mostrar_resultado_icono(resultado)

        # Actualizar imagen de la computadora
        self.actualizar_imagen_computadora(eleccion_computadora)

        # Verificar si el jugador ha ganado
        if self.puntaje_jugador == 5:
            messagebox.showinfo("Fin del juego", "¡Felicidades, ganaste el juego!")
            self.reiniciar()

    def reiniciar(self):
        """Reinicia el juego"""
        self.puntaje_jugador = 0
        self.puntaje_computadora = 0
        self.racha_jugador = 0
        self.resultado_label.config(text="Selecciona una opción")
        self.seleccion_computadora_label.config(text="Computadora elige...")
        self.puntaje_label.config(text=f"Puntaje - Jugador: {self.puntaje_jugador}  Computadora: {self.puntaje_computadora}")
        self.racha_label.config(text=f"Racha: {self.racha_jugador} victorias")
        self.imagen_computadora_label.config(image=self.img_piedra)

    def iniciar(self):
        """Inicia la interfaz gráfica"""
        self.ventana.mainloop()

# Crear una instancia del juego y ejecutarlo
if __name__ == "__main__":
    juego = JuegoPiedraPapelTijera()
    juego.iniciar()
