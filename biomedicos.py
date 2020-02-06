import requests
from bs4 import BeautifulSoup
import sys

print(sys.version)
name = input("Your Name?")

print("Hello", name)


URL = "https://www.occ.com.mx/empleos/de-ingenieria-biomedica/en-mexico/"

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
print(results)
