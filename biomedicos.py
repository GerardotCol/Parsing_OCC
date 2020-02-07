import requests
from bs4 import BeautifulSoup
import csv

# static HTML content

# URL = "https://www.occ.com.mx/empleos/de-ingenieria-biomedica/en-mexico/"
url_1 = "https://www.computrabajo.com.mx/ofertas-de-trabajo/p="
location = "estado-de-mexico"
empleo = "programador"

csv_file = open("cms_scrape.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Vacante", "Resumen", "Empresa", "Estado"])

# results = soup.find(id="ResultsContainer")
# print(soup.find(class="bRS bClick ")){}{}[]
for i in range(1, 10):

    url = (
        "https://www.computrabajo.com.mx/ofertas-de-trabajo/?p="
        + str(i)
        + "&q="
        + str(empleo)
    )
    print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    for oferta in soup.find_all("div", class_="bRS bClick"):
        vacante = oferta.h2.text
        resumen = oferta.p.text
        empresa = oferta.div.div.a.text
        estado = oferta.div.div.span.next_sibling.next_sibling.a.text

        csv_writer.writerow([vacante, resumen, empresa, estado])

csv_file.close()

