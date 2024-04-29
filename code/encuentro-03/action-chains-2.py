from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Inicializar el navegador
driver = webdriver.Chrome()

# Abrir la página web
driver.get("https://raw.githubusercontent.com/jumafernandez/soco-web_scraping/main/data/encuentro-03/drag-and-drop.html")

# Encontrar los elementos draggable y droppable
draggable_element = driver.find_element_by_id("draggable")
droppable_element = driver.find_element_by_id("droppable")

# Crear una instancia de ActionChains
action_chains = ActionChains(driver)

# Arrastrar y soltar el elemento draggable en el droppable
action_chains.drag_and_drop(draggable_element, droppable_element).perform()

# Esperar unos segundos para ver el resultado
driver.implicitly_wait(3)

# Cerrar el navegador
driver.quit()
