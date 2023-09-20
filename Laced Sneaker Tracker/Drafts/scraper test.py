import requests
from bs4 import BeautifulSoup

url = "https://laced.com/search?q=dunks"
result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")

names = doc.find_all(string="£")
print(names)
