from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import messagebox
import time

def ejecutar(username, password):
    if username and password:  # Verifica que se hayan proporcionado los datos
        driver = webdriver.Chrome()
        
        try:
            # Accede a la página de inicio de sesión
            messagebox.showinfo("Progreso", "Accediendo a la página de inicio de sesión...")
            driver.get("https://qa.dyalogo.cloud/manager/login")
            
            # Busca el campo de nombre de usuario
            try:
                # messagebox.showinfo("Progreso", "Buscando el campo de nombre de usuario...")
                name = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, '//*[@id="Login"]/div[2]/form/div[1]/input'))
                )
                name.send_keys(username)
            except Exception:
                messagebox.showerror("Error", "Error al encontrar o rellenar el campo de nombre de usuario")
                return

            # Busca el campo de contraseña
            try:
                # messagebox.showinfo("Progreso", "Buscando el campo de contraseña...")
                password_input = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, '//*[@id="Login"]/div[2]/form/div[2]/input'))
                )
                password_input.send_keys(password)
            except Exception:
                messagebox.showerror("Error", "Error al encontrar o rellenar el campo de contraseña")
                return

            # Hace clic en el botón de inicio de sesión
            try:
                # messagebox.showinfo("Progreso", "Buscando el botón de inicio de sesión...")
                login_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="Login"]/div[2]/form/div[3]/div[2]/button'))
                )
                login_button.click()
                # messagebox.showinfo("Progreso", "Iniciando sesión...")
            except Exception:
                messagebox.showerror("Error", "Error al hacer clic en el botón de inicio de sesión")
                return

            # Espera a que la página cargue completamente
            time.sleep(5)  # Ajusta este tiempo si es necesario
            messagebox.showinfo("Éxito", "Inicio de sesión completado con éxito")
        
        except Exception as e:
            messagebox.showerror("Error General", f"Ocurrió un error inesperado: {str(e)}")
        
        finally:
            driver.quit()
    else:
        messagebox.showerror("Error de Validación", "Los datos no son válidos. Por favor, verifica el nombre de usuario y la contraseña.")
