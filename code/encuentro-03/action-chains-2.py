from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

# Inicializar el navegador
driver = webdriver.Chrome()

# Abrir la página web
URL = "https://jumafernandez.github.io/soco-web_scraping/data/encuentro-03/drag-and-drop.html"
driver.get(URL)

# Encontrar los elementos draggable y droppable
draggable_element = driver.find_element(By.ID, "draggable")
droppable_element = driver.find_element(By.ID, "droppable")

# Crear una instancia de ActionChains
action_chains = ActionChains(driver)

# Esperar unos segundos para realizar la acción
time.sleep(3)

# Arrastrar y soltar el elemento draggable en el droppable
action_chains.drag_and_drop(draggable_element, droppable_element).perform()

# Esperar unos segundos para ver el resultado
time.sleep(3)

# Cerrar el navegador
driver.quit()
