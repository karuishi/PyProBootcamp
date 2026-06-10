from bs4 import BeautifulSoup
import requests

# --- Example 1: Parsing a local HTML file ---
# with open("website.html") as file:
#     contents = file.read()
    
# # We specify "html.parser" so Beautiful Soup knows what kind of document it is reading
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.p)

# # Find the FIRST occurrence of a specific tag
# first_anchor_tag = soup.find(name="a")
# print(first_anchor_tag.getText()) # Extracts the text inside the tag
# print(first_anchor_tag.get("href")) # Extracts the value of a specific attribute

# # Find ALL occurrences of a tag (returns a Python list)
# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#     print(tag.getText())
    
# # Find an element by its ID (Since IDs are unique, use find, not find_all)
# heading = soup.find(name="h1", id="name")
# # Find elements by Class name 
# # (Notice the underscore in class_! This is because 'class' is a reserved keyword in Python)
# section_heading = soup.find(name="h3", class_="heading")

# # Find the first <a> tag sitting directly inside a <p> tag
# company_url = soup.select_one(selector="p a")
# # Find an element by ID using the CSS # symbol
# name = soup.select_one(selector="#name")
# # Find ALL elements with a specific class using the CSS . symbol (returns a list)
# headings = soup.select(selector=".heading")

# --- Example 2: Parsing a live website ---
response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

# Find the FIRST articles Title, link, and upvotes count
# article_tag = soup.select_one(selector=".titleline a")
# article_title = article_tag.getText()
# article_link = article_tag.get("href")
# article_upvote = soup.select_one(".score").getText()

# print(article_title)
# print(article_link)
# print(article_upvote)

# Find ALL the articles Titles, links, and upvotes
# Using the CSS selector "> a" means "find the 'a' tag that is a direct child of the .titleline class"
articles = soup.select(".titleline > a")
articles_texts = []
articles_links = []
most_voted_article = []
for article_tag in articles:
    text = article_tag.getText()
    articles_texts.append(text)
    link = article_tag.get("href")
    articles_links.append(link)
    
article_upvotes = [int(score.getText().split()[0]) for score in soup.select(".score")]

# print(articles_texts)
# print(articles_links)
# print(article_upvotes)

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(articles_texts[largest_index])
print(articles_links[largest_index])
print(largest_number)