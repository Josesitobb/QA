from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time
import random

nombres_prueba = ([
    "AlejandroPrueba", "SofíaPrueba", "MateoPrueba", "ValentinaPrueba", "SantiagoPrueba",
    "IsabellaPrueba", "SebastiánPrueba", "CamilaPrueba", "NicolásPrueba", "MartinaPrueba",
    "DanielPrueba", "LucíaPrueba", "DiegoPrueba", "EmiliaPrueba", "SamuelPrueba",
    "GabrielaPrueba", "ÁngelPrueba", "PaulaPrueba", "JavierPrueba", "AnaPrueba",
    "AntonioPrueba", "ElenaPrueba", "CarlosPrueba", "SaraPrueba", "AndrésPrueba",
    "NataliaPrueba", "LeonardoPrueba", "ClaudiaPrueba", "RafaelPrueba", "TeresaPrueba",
    "ManuelPrueba", "LorenaPrueba", "FernandoPrueba", "LauraPrueba", "IvánPrueba",
    "ÁngelaPrueba", "RobertoPrueba", "AdrianaPrueba", "LuisPrueba", "PatriciaPrueba",
    "EnriquePrueba", "SandraPrueba", "TomásPrueba", "VictoriaPrueba", "MarioPrueba",
    "AntoniaPrueba", "MiguelPrueba", "RosaPrueba", "HugoPrueba", "JuliaPrueba"
])
def ejecutar(cantidad):
    driver = webdriver.Chrome()
    driver.get("https://qa.dyalogo.cloud/manager/login.php")
    driver.set_window_size(1382, 744)

    element = driver.find_element(By.CSS_SELECTOR, ".hold-transition")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = driver.find_element(By.CSS_SELECTOR, ".hold-transition")
    actions.move_to_element(element).perform()
    element = driver.find_element(By.CSS_SELECTOR, ".hold-transition")
    actions.move_to_element(element).release().perform()
    driver.find_element(By.CSS_SELECTOR, ".hold-transition").click()
    #USUARIO NUEVO
    usuario="12312312"
    driver.find_element(By.NAME, "txtUsuario").send_keys(usuario)
    driver.find_element(By.CSS_SELECTOR, ".hold-transition").click()
    #CONTRASEÑA
    contraseña="1232"
    driver.find_element(By.NAME, "txtPassword").send_keys(contraseña)
    driver.find_element(By.CSS_SELECTOR, ".col-xs-4 > .btn").click()

    driver.find_element("xpath", '/html/body/div[8]/aside/section/ul/li[2]/a/i').click()

    try:
        # Hacer clic en "add" 5 veces
        for _ in range(cantidad):
            nombre_usuario = random.choice(nombres_prueba)  # Aquí usa random.choice correctamente
            documento = random.randint(1000, 1000000)
            correo=str(random.randint(5100,99999))


            driver.find_element(By.ID, "add").click()
            time.sleep(2)

            # Llenar el formulario con los datos proporcionados
            driver.find_element(By.ID, "NombreUsuario").click()
            driver.find_element(By.ID, "NombreUsuario").send_keys(nombre_usuario)
            time.sleep(2)
            driver.find_element(By.ID, "Correo").click()
            driver.find_element(By.ID, "Correo").send_keys(nombre_usuario+correo+"@gmail.com")
            time.sleep(2)
            driver.find_element(By.ID, "IdentificacionUsuario").click()
            driver.find_element(By.ID, "IdentificacionUsuario").send_keys(documento)
            time.sleep(2)
            driver.find_element(By.ID, "Cargo").click()
            dropdown = Select(driver.find_element(By.ID, "Cargo"))
            dropdown.select_by_visible_text("Agente")
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, "#FormularioDatos > .panel:nth-child(2) > .box-header").click()
            driver.find_element(By.LINK_TEXT, "Datos laborales").click()
            time.sleep(2)
        # Selección del tipo de contrato
            driver.find_element(By.ID, "tipoContrato").click()
            dropdown = Select(driver.find_element(By.ID, "tipoContrato"))
            dropdown.select_by_index(3)  # Selecciona el cuarto elemento (índice 3)
            driver.find_element(By.LINK_TEXT, "Datos laborales").click()
            time.sleep(2)
        # Selección de horario y doble clic
            driver.find_element(By.ID, "Horario").click()
            element = driver.find_element(By.ID, "Horario")
            actions = ActionChains(driver)
            actions.double_click(element).perform()
            time.sleep(2)
        # Guardar los datos
            driver.find_element(By.ID, "Save").click()
            time.sleep(8)
    except NoSuchElementException as e:
        print(f"Error: No se encontró el elemento: {e}")
  
