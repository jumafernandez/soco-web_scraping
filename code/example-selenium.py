from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()

# Los dos primeros son mutuamente excluyentes
# options.add_argument("--window-size=1920,1080")  # Establecer tamaño de ventana
options.add_argument("--start-maximized")  # Maximiza la ventana al abrir
# options.add_argument("--headless")  # Ejecución de las acciones sin interfaz visual
# options.add_argument("--disable-extensions")  # Deshabilita las extensiones
# options.add_argument("--blink-settings=imagesEnabled=false") # Desactiva la carga de imágenes
# options.add_argument("--disable-autofill") # Desactiva la función de autocompletado
# Desactiva el guardado automático de claves
# options.add_argument("--disable-password-manager-reauthentication") 
# options.add_argument("--lang=es")  # Inicia Chrome en español

# prefs = {"download.default_directory": "/downloads"}  # Establece el directorio de descargas
# options.add_experimental_option("prefs", prefs)
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)

import time

# Inicializo el driver
driver = webdriver.Chrome()

# Se debe pasar el protocolo completo en la URL (http, https, etc)
# driver.get('https://bowen.com.ar/')

# print(contenido_html)



# Se debe pasar el protocolo completo en la URL (http, https, etc)
# ID = 1
# URL_id = f'https://bowen.com.ar/coleccion/invierno-23/ver-todo.html?p={ID}'
# driver.get(URL_id)

# time.sleep(3) # Se espera 3 segundos

# Se hace el get a otro sitio distinto
# driver.get('http://www.unlu.edu.ar')
# time.sleep(3) # Se espera 3 segundos

# Se vuelve al sitio de Bowen
# driver.back()
# time.sleep(3) # Se espera 3 segundos

# Se pasa nuevamente al de la UNLu
# driver.forward()
# time.sleep(3) # Se espera 3 segundos

# Se refresca la página
# driver.refresh()

# driver.close() # Cierra la ventana
# driver.quit() # Cierra el driver completamente

URL = 'https://bowen.com.ar/coleccion/invierno-23/ver-todo.html'
driver.get(URL)

input_moneda = driver.find_element(By.ID, "current-currency-code")
input_moneda_valor = input_moneda.get_attribute('value')

#print(f'La moneda actual es {input_moneda_valor}')

time.sleep(10) # Se espera 10 segundos

#contenido_html = driver.page_source

# Encontrar todos los elementos div con la clase "product details product-item-details"
elementos_div = driver.find_elements(By.CLASS_NAME, "product.details.product-item-details")

elementos_div = driver.find_elements(By.CSS_SELECTOR, "div.product.details.product-item-details")


# Iterar sobre cada elemento para capturar su contenido
# for elemento in elementos_div:
#    contenido = elemento.text
#    print(contenido)

# Encontrar todos los elementos <a> (enlaces) utilizando By.TAG_NAME
enlaces = driver.find_elements(By.TAG_NAME, 'a')
for e in enlaces:
    if e.text!='': # Si tienen texto, los muestra
        
        # Obtener atributos específicos del enlace
        href = e.get_attribute("href")
        clase = e.get_attribute("class")
        id_enlace = e.get_attribute("id")
        title = e.get_attribute("title")
        
        # Obtener todos los atributos del enlace
        print(f"Atributo href: {href}")
        print(f"Atributo class: {clase}")
        print(f"Atributo id: {id_enlace}")
        print(f"Atributo title: {title}")        
        
        
        
        
        
        
        