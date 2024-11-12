import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
import importlib

# Diccionario de pruebas y sus requerimientos de datos
pruebas = {
    "Prueba De Login": {"archivo": "prueba_login", "necesita_datos": True},
    "Prueba De Creacion Usuario":{"archivo":"prueba_creacion_usuarios","necesita_datos":True},
    "Prueba De Edicion Usuario":{"archivo":"prueba_edicion_usuario","necesita_datos":True},
    
}


def ejecutar_prueba():
    prueba_seleccionada = seleccion.get()
    if prueba_seleccionada in pruebas:
        prueba_info = pruebas[prueba_seleccionada]
        archivo_prueba = prueba_info["archivo"]
        necesita_datos = prueba_info["necesita_datos"]
        
        # Importa el módulo de prueba
        modulo = importlib.import_module(archivo_prueba)
        
        # Si la prueba necesita datos, los solicita al usuario
        if necesita_datos:
            # Solicita datos dependiendo de la prueba seleccionada
            if prueba_seleccionada == "Prueba De Login":
                username = simpledialog.askstring("Input", "Ingresa el nombre de usuario:")
                password = simpledialog.askstring("Input", "Ingresa la contraseña:", show="*")
                if username and password:
                    try:
                        modulo.ejecutar(username, password)
                        messagebox.showinfo("Resultado", f"{prueba_seleccionada} completada")
                    except Exception as e:
                        messagebox.showerror("Error", f"No se pudo ejecutar la prueba: {e}")
                else:
                   
                    messagebox.showwarning("Advertencia", "No se ingresaron todos los datos requeridos")
           
           
            #PRUEBA DE USUARIOS
            elif prueba_seleccionada == "Prueba De Creacion Usuario":
                try:
                    cantidad_str = simpledialog.askstring("Input", "Ingresa la cantidad de usuarios:")
                    if cantidad_str is None:
                        messagebox.showinfo("Info", "Operación cancelada.")
                    else:
                        cantidad = int(cantidad_str)
                        if cantidad > 0:
                            modulo.ejecutar(cantidad)
                            # messagebox.showinfo("Info", f"Cantidad ingresada: {cantidad}")
                            messagebox.showinfo("Éxito", f"Se han creado {cantidad} usuarios.")

                            
                            # Aquí puedes llamar a la función o el módulo para ejecutar la prueba
                            # Ejemplo: modulo.ejecutar(cantidad)
                        else:
                            messagebox.showwarning("Advertencia", "La cantidad debe ser mayor a cero.")
                except ValueError:
                        messagebox.showerror("Error", "Por favor, ingresa un número válido.")


            elif prueba_seleccionada == "Prueba De Edicion Usuario":
                Correo_Buscar = simpledialog.askstring("Input", "Ingresa el nombre de usuario:")
                if Correo_Buscar:
                    try:
                        modulo.ejecutar(Correo_Buscar)
                        messagebox.showinfo("Resultado", f"{prueba_seleccionada} completada")
                    except Exception as e:
                        messagebox.showerror("Error", f"No se pudo ejecutar la prueba: {e}")
                else:
                    messagebox.showwarning("Advertencia", "No se ingresaron todos los datos requeridos")
    
            # Aquí puedes agregar más condiciones para otras pruebas que requieran datos
        else:
            # Si no necesita datos, ejecuta la prueba directamente
            try:
                modulo.ejecutar()
                messagebox.showinfo("Resultado", f"{prueba_seleccionada} completada")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo ejecutar la prueba: {e}")
    else:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una prueba")


# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Ejecutor de Pruebas Automáticas")
ventana.geometry("300x200")
ventana.configure(bg="lightblue")  # Color de fondo

# Label de instrucciones
tk.Label(ventana, text="Selecciona una prueba para ejecutar:", bg="lightblue", fg="navy", font=("Arial", 12)).pack(pady=10)

# Menú desplegable para seleccionar la prueba
seleccion = tk.StringVar()
menu_pruebas = ttk.Combobox(ventana, textvariable=seleccion, values=list(pruebas.keys()), state="readonly")
menu_pruebas.pack(pady=10)

# Estilo del botón
estilo_boton = ttk.Style()
estilo_boton.configure("TButton", font=("Arial", 10), padding=10, relief="flat")
estilo_boton.map("TButton",
                 background=[("active", "green"), ("!active", "lightgreen")],
                 foreground=[("active", "white"), ("!active", "black")])

# Botón para iniciar la prueba seleccionada
boton_ejecutar = ttk.Button(ventana, text="Iniciar Prueba", command=ejecutar_prueba, style="TButton")
boton_ejecutar.pack(pady=20)

# Iniciar el loop de la interfaz
ventana.mainloop()