from bs4 import BeautifulSoup

with open(file= "website.html", mode= "r") as data:
    content = data.read()

data = BeautifulSoup(markup= content, features= "html.parser")
stuff = data.find_all(name= "h3")
for i in stuff:
    print(i.string)

data.find(name= "h3")