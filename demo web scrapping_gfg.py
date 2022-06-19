import stringprep
import requests
from bs4 import BeautifulSoup

#step1:get the html
r = requests.get("https://practice.geeksforgeeks.org/home/")
htmlContent = r.text
#print(htmlContent)

#step2:parse the html
soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify())

#step3:html tree traveral
#commonly used types of objects
#4.comment
title=soup.title#get the title of html page
print(title)
print(type(title.string))#navigable string
print(type(soup))#beautiful soup
print(type(title))#tag

#get all the paragraphs from the page
paras = soup.find_all('p')
print(paras)

#get first element from the Html page and the class
print(soup.find('p')['class'])

#get all elements with clss lead
print(soup.find_all("p", class_="lead"))

#get all text of page
print(soup.get_text())

#get all text from tag/soup
print(soup.find('p').get_text())

#get all the anchor tags from the page
anchors = soup.find_all('a')
print(anchors)
all_links = set()
#get all links on the page
#for link in anchors:
 #   if(link.get('href') != '#'):
   #     linkText = "https://practice.geeksforgeeks.org/home/" +link.get('href')
   #     all_links.add(link)
    #    print(linkText)

displayModal = soup.find(id='displayModal')

for elem in displayModal.contents:
    print(elem)

for item in displayModal.strings:
    print(item)

for item in displayModal.stripped_strings:
    print(item)

print(displayModal.parent)

print(displayModal.parents)
for item in displayModal.parents:
    print(item.name)

print(displayModal.next_sibling.next_sibling)

print(displayModal.previous_sibling.previous_sibling)

elem = soup.select('.displayModal')
print(elem)


