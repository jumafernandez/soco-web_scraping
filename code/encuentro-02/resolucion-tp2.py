from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializar el navegador Chrome
driver = webdriver.Chrome()

# Cargar la página del formulario
URL = 'https://jumafernandez.github.io/soco-web_scraping/data/formulario-tp.html'
driver.get(URL)

# Esperar a que el formulario se cargue completamente
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "formulario")))

# Ingresar el correo electrónico y la contraseña
email_input = driver.find_element(By.ID, "email")
email_input.send_keys("correo@example.com")

passwd_input = driver.find_element(By.ID, "passwd")
passwd_input.send_keys("contraseña123")

# Seleccionar el país "Brasil"
pais_select = driver.find_element(By.ID, "pais")
brasil_option = pais_select.find_element(By.XPATH, "//option[contains(text(), 'Brasil')]")
brasil_option.click()

# Hacer clic en el checkbox "Recordar Usuario"
recordar_checkbox = driver.find_element(By.ID, "recordar")
recordar_checkbox.click()

# Hacer clic en el botón "Ingresar"
ingresar_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
ingresar_button.click()

# Esperar a que se cargue la página siguiente (si hay una)
# Aquí puedes agregar más código para interactuar con la página siguiente si es necesario
