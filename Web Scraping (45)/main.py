from bs4 import BeautifulSoup
import requests

# with open(file= "website.html", mode= "r") as data:
#     content = data.read()

# # ------------------------ Create BeautifulSoup Object ----------------------- #
# data = BeautifulSoup(markup= content, features= "html.parser")

# -- Use find_all method to find all h3 and loop to get the strings in them -- #
# stuff = data.find_all(name= "h3")
# for i in stuff:
#     print(i.string)

# ------------------- Use find method to find the first h3 ------------------- #
# data.find(name= "h3")

# --------------- Getting the first anchor element and its href -------------- #
# print(data.find(name= "a").get("href"))
# print(data.a.get("href"))

# # --------- Get a specific elements href by using CSS-Selector syntax -------- #
# print(data.select(selector= "body p em strong a")[0].get("href"))

"""
The select() method is by far the best since you can use CSS-Selection just like in CSS
"""

# ---------------------- Work with live data from a site --------------------- #

# response = requests.get(url="https://www.seanhalpin.xyz/")
# response.raise_for_status()
# response_content = response.content

# markup_soup = BeautifulSoup(markup= response_content, features= "html.parser")
# # print(markup_soup.find(name= "title").string)
# print(markup_soup.find(name= "meta", property= "og:image").get("content"))

# ------------------------- Second, more complex site ------------------------ #
response = requests.get(url="https://news.ycombinator.com/")
response.raise_for_status()
response_content = response.content

markup_soup = BeautifulSoup(markup= response_content, features= "html.parser")
sought_content = markup_soup.find_all(class_= "titleline")

content_titlelines = []
content_urls = []
for i in sought_content:
    content_titlelines.append(i.find(name= "a").string)
    content_urls.append(i.find(name= "href"))
    