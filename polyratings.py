import requests
from requests import get
from bs4 import BeautifulSoup

page = requests.get(
        "https://www.polyratings.com/eval/"
        + str(3352)
        + "/index.html"
    )

soup = BeautifulSoup(page.text, 'html.parser')
results = soup.find(class_='col-xs-12')
name = results.strong.text

results = soup.find(class_='col-xs-4 hidden-xs')
soup.find_all("a")
print(results.h2.text)

#name = results.strong.text
