from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

CANTIDAD_ITERACIONES = 3

options = Options()
options.add_argument("--headless")  # Ejecución de las acciones sin interfaz visual

# Inicializo el driver
driver = webdriver.Chrome(options=options)

# Conjunto para almacenar URLs de productos ya procesados
productos_procesados = set()
productos_repetidos = 0
gets_sin_actualizacion = 0

for id_p in range(1, 1000):
    
    # Se genera la URL con cada id
    URL = f'https://bowen.com.ar/coleccion/invierno-23/ver-todo.html?p={id_p}'
    driver.get(URL)
    
    print(f'\nIteración {id_p+1}: {URL}')
    
    # Encontrar todos los elementos div con la clase "product details product-item-details"
    items = driver.find_elements(By.CLASS_NAME, "product.details.product-item-details")
    
    # Se contabilizan los productos agregados en cada get
    productos_agregados = 0
    
    for producto in items:
        # Obtengo la info con el enlace de cada item (en el enlace también está la descripción)
        enlace_a = producto.find_element(By.CLASS_NAME, "product-item-link")
        link_producto = enlace_a.get_attribute("href")
        
        # Verificar si el enlace ya ha sido procesado antes
        if link_producto in productos_procesados:
            productos_repetidos += 1
            continue  # Pasar al siguiente producto si ya ha sido procesado
        else:
            productos_agregados += 1
        
        descripcion = enlace_a.text
        
        # Encuentro el precio que está en el span de class='price' dentro de otro span 'finalPrice'
        xpath_precio = "//span[@data-price-type='finalPrice']/span[@class='price']"
        # Esperar a que el elemento esté presente en la página
        precio_elemento = producto.find_element(By.XPATH, xpath_precio)
        precio = precio_elemento.text
    
        # Agregar la URL del producto actual al conjunto de productos procesados
        productos_procesados.add(link_producto)
    
        print(f'{descripcion}: {precio} ({link_producto})')

    print(f'Productos incorporados: {productos_agregados}.')
    
    if productos_agregados == 0:
        gets_sin_actualizacion += 1
        if gets_sin_actualizacion == CANTIDAD_ITERACIONES:
            print(f'\n{CANTIDAD_ITERACIONES} sin productos nuevos. Se finaliza con el web scraping.')
            break
    else:
        gets_sin_actualizacion = 0
        

driver.close()
