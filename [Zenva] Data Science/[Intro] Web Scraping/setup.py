from bs4 import BeautifulSoup
import requests

# HTML test code
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# Applying the BeautifulSoup function to the variable html_doc then assigning that to the variable soup
soup = BeautifulSoup(html_doc)
print(soup.title)
print(soup.p)

# Test the request function
response = requests.get("https://www.wikipedia.org/")
print(response.text)