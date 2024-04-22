from seleniumwire import webdriver

# Configuración de las opciones del proxy
proxy_options = {
    'proxy': {
        'http': 'http://209.126.6.159:80',
        'https': 'https://209.126.6.159:80',
        'no_proxy': 'localhost,127.0.0.1' 
        # no_proxy es opcional: lista de hosts a los que no aplica proxy
    }
}

# Crear el driver de Selenium con las opciones del proxy
driver = webdriver.Chrome(seleniumwire_options=proxy_options)

# Ejemplo de uso del driver con el proxy configurado
driver.get('https://www.google.com')

# Cerrar el driver al finalizar
driver.quit()
