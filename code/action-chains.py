from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Inicializar el driver
driver = webdriver.Chrome()

# Abrir la página web
driver.get("https://jumafernandez.github.io/soco-web_scraping/data/html-actionchains.html")

# Encontrar los elementos sobre los cuales realizar la acción
box1 = driver.find_element(By.ID, "box1")
box2 = driver.find_element(By.ID, "box2")
box3 = driver.find_element(By.ID, "box3")

# Inicializar ActionChains
actions = ActionChains(driver)

# Ejemplo 1: Hacer clic derecho en Box 1
actions.context_click(box1).perform()
time.sleep(5)

# Ejemplo 2: Hacer doble clic en Box 2
actions.double_click(box2).perform()
time.sleep(5)

# Ejemplo 3: Arrastrar Box 3 a Box 1
actions.drag_and_drop(box3, box1).perform()
time.sleep(5)

# Ejemplo 4: Mover el mouse a Box 2
actions.move_to_element(box2).perform()
time.sleep(5)

# Ejemplo 5: Presionar la tecla Shift mientras hacemos clic en Box 3
actions.key_down(Keys.SHIFT).click(box3).key_up(Keys.SHIFT).perform()
time.sleep(5)

# Cerrar el navegador al finalizar
driver.quit()
