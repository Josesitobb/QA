from selenium import webdriver

def ejecutar():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    # Aquí se añaden los pasos de la prueba de búsqueda
    driver.quit()
    print("Prueba de Búsqueda completada")
