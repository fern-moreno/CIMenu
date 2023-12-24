import requests
import io
from bs4 import BeautifulSoup
from pypdf import PdfReader

csuci_url= 'https://uas.csuci.edu/hospitality/hospitality-locations.htm'
html_text = requests.get(csuci_url).text
soup = BeautifulSoup(html_text, 'html.parser')

pdfs = []
for a in soup.find_all('a', href=True):
     if a['href'].endswith('.pdf'):
        pdfs.append(a['href'])

menu_url = 'https://uas.csuci.edu/' + pdfs[0]
print(menu_url)

r = requests.get(menu_url)
f = io.BytesIO(r.content)

reader = PdfReader(f)
contents = reader.pages[0].extract_text().split('\n')
print(contents)

