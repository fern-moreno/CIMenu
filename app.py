import requests
from bs4 import BeautifulSoup

menu_url = 'https://uas.csuci.edu/hospitality/hospitality-locations.htm'
html_text = requests.get(menu_url).text
soup = BeautifulSoup(html_text, 'html.parser')

for a in soup.find_all('a', href=True):
     if a['href'].endswith('.pdf'):
        print(a['href'])
