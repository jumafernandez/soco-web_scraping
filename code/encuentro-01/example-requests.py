import requests

# Se realiza una solicitud GET a la URL
URL = 'https://raw.githubusercontent.com/jumafernandez/soco-web_scraping/main/data/example-01.html'
r = requests.get(URL)
# Es posible desactivar potenciales redirecciones
# r = requests.get('URL', allow_redirects=False)

# Es posible verificar el estado del request
if r.status_code == 200:
    print("El request fue realizado correctamente")
else:
    print("El request arrojó error con el siguiente estado: ", r.status_code)

# Se imprimen los headers de la respuesta HTTP en un dict
print(r.headers)

# Se imprime el contenido de la web
print(r.text)

from bs4 import BeautifulSoup

html_content = r.text
    
soup = BeautifulSoup(html_content, 'html.parser')
    
links = soup.find_all('a')
    
# Imprimir los enlaces encontrados
for link in links:
    print(link.get('href'))
    
    
# Encontrar los elementos <td> con clase "marca"
elements = soup.find_all('td', class_='marca')
    
# Imprimir los elementos encontrados
for element in elements:
    if element.text[-1] == 'o':
        print(element.text)
