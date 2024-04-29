from selenium import webdriver
from fake_useragent import UserAgent

# Muestro 5 ejemplos de user agent
for i in range(1, 5):
    user_agent = UserAgent().random
    print(user_agent)

# Incoporo un user agent en el GET
driver = webdriver.Chrome()
user_agent = UserAgent().random
headers = {'User-Agent': user_agent}
driver.get('https://www.carrefour.com.ar', headers=headers)
    
    