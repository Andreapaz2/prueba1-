import tkinter as tk 
from views.cargar_vistas import cargar_usuario
ventana = tk.Tk()
ventana.title("Filtrar Datos")
ventana.geometry("1000x500")

cargar_usuario(ventana)

ventana. mainloop()