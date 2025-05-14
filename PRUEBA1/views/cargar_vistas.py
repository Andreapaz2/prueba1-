import tkinter as tk 
from CONECTARSQL.conectarsql import conectar

def cargar_usuario(ventana):
    login_panel = tk.Frame(
        ventana,
        bg="green",
        padx=0,
        pady=0,
        width=1200,
        height=600
        )
    
    titulo = tk.Label(login_panel, text="Filtrar Datos")
    titulo.pack()
    
    txt_correo = tk.Label(login_panel, text="Usuario")
    txt_correo.pack()

    entrada_correo = tk.Entry(login_panel)
    entrada_correo.pack()


    def funcion_boton():
        usuario_login = entrada_correo.get()
        print("Usuario: ",usuario_login)
        print(conectar(f"""SELECT * FROM usuarios WHERE nombres = '{usuario_login}'"""))


    boton = tk.Button(login_panel, text = "Continuar",command=funcion_boton)
    boton.pack()


    login_panel.pack()
    print("Panel login cargado")
