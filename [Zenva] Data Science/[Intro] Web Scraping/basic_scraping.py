from bs4 import BeautifulSoup

# Learning basic BeautifulSoup functionality


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

soup = BeautifulSoup(html_doc, "html.parser")

# soup dot notation
# print(soup.prettify())

# print(soup.title)

# print(soup.title, '\n')
# print(soup.title.string)


# print(soup.p.b)

# print(soup.p['class'])
# print(soup.a['href'])

# "Find" function
# print(soup.find(href="http://example.com/lacie"))
# print(soup.find(class_="story"))

# "Find All" function
""" a_tags = soup.find_all('a')
print(a_tags) """

# Finds the 3rd item in the list
# print(a_tags[2])

# Finds both the 'a' and 'title' tags
# a_title_tags = soup.find_all(['a', 'title'])


# Taversing the Tree Part 1
p = soup.find(class_="story")

# Returning contents of a tag as a list
# print(p.contents)

# Access the contents in the form of an iterator
#for child in p.children:
#   print(child)

# Cast the descendants to a list
body = soup.find('body')
"""descendants = list(body.descendants)
print(descendants)
print(len(descendants))"""


# Traversing the Tree Part 2

# Navigating to Parent Tags
""" # This gets us the first 'a' tag in the HTML
a = soup.a 
#This will print the parent of the 'a' tag
print(a.parent)"""

# Getting All Parents of a Tag
"""for p in soup.a.parents:
    print (p.name)"""

# Accessing Siblings
"""a = soup.a  # The first 'a' tag
print(a.next_sibling.next_sibling)  # This will print the second 'a' tag"""

"""a = soup.a.next_sibling.next_sibling  # The second 'a' tag
print(a.previous_sibling.previous_sibling)  # This will print the first 'a' tag"""