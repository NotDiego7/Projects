from bs4 import BeautifulSoup

with open(file= "website.html", mode= "r") as data:
    content = data.read()

# ------------------------ Create BeautifulSoup Object ----------------------- #
data = BeautifulSoup(markup= content, features= "html.parser")

# -- Use find_all method to find all h3 and loop to get the strings in them -- #
# stuff = data.find_all(name= "h3")
# for i in stuff:
#     print(i.string)

# ------------------- Use find method to find the first h3 ------------------- #
# data.find(name= "h3")

# --------------- Getting the first anchor element and its href -------------- #
# print(data.find(name= "a").get("href"))
# print(data.a.get("href"))

# --------- Get a specific elements href by using CSS-Selector syntax -------- #
print(data.select(selector= "body p em strong a")[0].get("href"))

"""
The select() method is by far the best since you can use CSS-Selection just like in CSS
"""

