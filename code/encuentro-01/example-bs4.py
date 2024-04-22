import requests
from bs4 import BeautifulSoup

# Se realiza una solicitud GET a la URL
URL = 'https://raw.githubusercontent.com/jumafernandez/soco-web_scraping/main/data/example-bs4.html'
r = requests.get(URL)

# Paso a una variable el texto html
html_content = r.text
    
soup = BeautifulSoup(html_content, 'html.parser')

#print(soup)
#print(soup.prettify())

# Devuelve el primer elemento que cumple con el criterio especificado
primer_p = soup.find('p')

# Devuelve todos los elementos de un tipo especificado
all_ps = soup.find_all('p')
all_ps[0]

multiples_condiciones = soup.find_all('a', id='link1')

multiples_condiciones[0].attrs

multiples_condiciones[0].attrs['href']

multiples_condiciones[0].get_text()