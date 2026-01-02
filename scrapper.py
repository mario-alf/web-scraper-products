#Main script
# scraper.py
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de prueba
url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"

# Hacer la solicitud HTTP
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Lista para guardar productos
products = []

# Buscar productos en la página
for item in soup.select('.thumbnail'):
    name = item.select_one('.title').text.strip()
    price = item.select_one('.price').text.strip()
    description = item.select_one('.description').text.strip()
    products.append({
        'Name': name,
        'Price': price,
        'Description': description
    })

# Guardar en CSV
df = pd.DataFrame(products)
df.to_csv('examples/products_example.csv', index=False)

print("Scraping completed. CSV saved in /examples/")
