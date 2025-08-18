import requests
from bs4 import BeautifulSoup
import time
import string
import re
page_ = input("Which page would you like to scrape: ")
int_page = int(page_)

if int_page >= 1 and int_page <= 100:
    response = requests.get(f'https://annas-archive.org/search?index=&page={page_}&q=&display=&content=book_nonfiction&content=book_fiction&acc=aa_download&acc=external_download&lang=en&sort=')
else:
    input("An error has occured. Please enter another page: ")

soup = BeautifulSoup(response.content, 'html.parser')

links = soup.find_all('a')
divs_of_descriptions = soup.find_all('div', class_="line-clamp-[2] leading-[1.2] text-[10px] lg:text-xs text-gray-500")
titles_ = soup.find_all("h3", class_="max-lg:line-clamp-[2] lg:truncate leading-[1.2] lg:leading-[1.35] text-md lg:text-xl font-bold")
author_ = soup.find_all('div', class_="max-lg:line-clamp-[2] lg:truncate leading-[1.2] lg:leading-[1.35] max-lg:text-sm italic")
imgs_ = soup.find_all("img", class_="relative inline-block")
divs = soup.find_all('div')
md5s = []
titles = []
descriptions = []
imgs = []
authors = []

for i in links:
    if "/md5/" in i["href"]:
        md5 = i['href']
        md5_cleansed = md5.split("/")[-1]
        md5s.append(md5_cleansed)
    
for i in divs_of_descriptions:
    for i in i.contents:
        descriptions.append(i)

for i in author_:
    authors.append(i.contents)

for i in titles_:
    for i in i.contents:
        titles.append(i)
count_imgs = 0
for i in imgs_:
    imgs.append(i["src"])
    if len(imgs) < len(md5s):
        nulls = len(md5s) - len(imgs)
        while count_imgs < nulls:
            imgs.append("null")
            count_imgs+=1

total_books = len(md5s)
tot = total_books + 1
books = [[] for i in range(total_books)]
z = 0

for i in range(total_books):
    while z < (total_books):
        books[z].append(titles[z])
        books[z].append(md5s[z])
        books[z].append(authors[z])
        books[z].append(imgs[z])
        books[z].append(descriptions[z])
        z+=1

print("fetching results...")
time.sleep(3)
print(books)