from bs4 import BeautifulSoup
import requests

# Assign the requests function to a variable
response = requests.get('https://www.coursera.org/articles/data-analytics-projects-for-beginners')


soup = BeautifulSoup(response.text, "html.parser")

print(soup.text)
