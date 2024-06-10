from bs4 import BeautifulSoup
import requests

# Assign the requests function to a variable
response = requests.get('URL')


soup = BeautifulSoup(response.text, "html.parser")

print(soup.text)
