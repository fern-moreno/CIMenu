from pypdf import PdfReader
from twilio.rest import Client
from twilio.rest import Client
from twilio.rest import Client

import requests
import io
import os
from bs4 import BeautifulSoup

# twilio account information and linking
account_sid = 'AC5b43b62a3f22346398a7b34bdf67e953'
auth_token = '2cc6963cf9ebb3f8eba0100537728efa'
client = Client(account_sid, auth_token)

# csuci restaurant webpage and web scraper setup
csuci_url= 'https://uas.csuci.edu/hospitality/hospitality-locations.htm'
html_text = requests.get(csuci_url).text
soup = BeautifulSoup(html_text, 'html.parser')

# finding links on website, extracting only the pdf files
pdfs = []
for a in soup.find_all('a', href=True):
     if a['href'].endswith('.pdf'):
        pdfs.append(a['href'])

# constucting the url to the menu pdf
menu_url = 'https://uas.csuci.edu/' + pdfs[0]
print(menu_url)


# reading the pdf menu
r = requests.get(menu_url)
f = io.BytesIO(r.content)

reader = PdfReader(f)
contents = reader.pages[0].extract_text().split('\n')

#constructing the text message to send with twilio
text = ""
for content in contents:
    text += content
    text += '\n'

#print(text)

# constructing the text and sending it
message = client.messages.create(body = text,  from_='+18334582114',
  to='+18083332789')

print(message.sid)