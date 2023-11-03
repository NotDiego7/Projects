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

# ------------- Second, more complex site (Get two title and url) ------------ #
# response = requests.get(url="https://news.ycombinator.com/")
# response.raise_for_status()
# response_content = response.content

# markup_soup = BeautifulSoup(markup= response_content, features= "html.parser")
# sought_content = markup_soup.find_all(class_= "titleline")

# content_extract = []
# for i in sought_content:
#     anchor_tag = i.find(name= "a")
#     content_extract.append([anchor_tag.string, anchor_tag.get("href")])

# print(content_extract)

# ------------ Get the first page's highest upvoted title and url ------------ #
# response = requests.get(url= "https://news.ycombinator.com/")
# response.raise_for_status()
# markup = response.content

# markup_soup = BeautifulSoup(markup= markup, features= "html.parser")
# all_sought_content = markup_soup.find_all(class_="score")

# upvote_points_list = [(int(i.string.split()[0])) for i in all_sought_content]

# upvote_points_list.sort(reverse= True)
# highest_upvoted = upvote_points_list[0]

# highest_upvoted_id = markup_soup.find(name= "span", class_= "score", string= f"{highest_upvoted} points").get("id").split("_")[1]

# highest_upvoted_element = markup_soup.find(name= "tr", id= highest_upvoted_id)
# highest_upvoted_element = highest_upvoted_element.find(name= "span", class_= "titleline").find("a")

# highest_upvoted_url = highest_upvoted_element.get("href")
# highest_upvoted_title = highest_upvoted_element.string

# print(f"{highest_upvoted_title}\n{highest_upvoted_url}\n{highest_upvoted}")

# ----------------------------------- Final ---------------------------------- #
response = requests.get(url= "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
markup = response.content

soup_obj = BeautifulSoup(markup= markup, features= "html.parser")

scrapped_list = soup_obj.find_all(name= "h3", class_= "title")
scrapped_list.reverse()
ordered_scrapped_string_list = [f"{i.string} \n" for i in  scrapped_list]

with open(file= "100 Top Films.txt", mode= "w") as f:
    f.writelines(ordered_scrapped_string_list)

#TODO: We need a list which contains list elements consisting of the rank from 1-100 and title of film