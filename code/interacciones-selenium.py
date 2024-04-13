from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicializo el driver
driver = webdriver.Chrome()

# Se debe pasar el protocolo completo en la URL (http, https, etc)
URL = 'https://jumafernandez.github.io/soco-web_scraping/data/formulario.html'
driver.get(URL)

# Localizo los input donde se debe ingresar la información
input_correo = driver.find_element(By.ID, "email")
input_clave = driver.find_element(By.ID, "passwd")

# Emulo el ingreso de la información
input_correo.send_keys('juanmanuelunlu@gmail.com')
input_clave.send_keys('888888')

input_correo.clear()
input_clave.clear()

# Emulo el ingreso de la información nuevamente
input_correo.send_keys('juanmanuelunlu@gmail.com')
input_clave.send_keys('888888')

# Localizo el botón de tipo submit por su atributo type y su valor
boton_ingresar = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
boton_ingresar.click()


