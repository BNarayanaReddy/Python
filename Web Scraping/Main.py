import requests as req
from bs4 import BeautifulSoup

# Using requests
r = req.get("https://www.google.com")

print(r.text)


# Using Local HTML files 

with open("Main.html","r") as obj:
    html_code=obj.read()




soup = BeautifulSoup(html_code,'html.parser')

souped = soup.prettify()
print(soup)


""" Accesing first occurence through tags reference """

print(soup.title)
print(soup.title.string)
print(soup.div.string)
print(soup.meta)


""" Accessing through tags along with the attributes using .get() """

print(soup.a.get("target"))
print(soup.a.get("href"))
print(soup.a.string)


""" Accesing tags across the program returns list """

print(soup.find_all("div"))
print(soup.find_all("div")[0])

for i in soup.find_all("a"):
    print(i.get("href"))

i = soup.find_all(class_ = "link")
print(i[0].get("href"))

lin = soup.find(class_ = "link")
print(lin.get("href"))


""" Simple Case referencing tags and classes returns list"""

print(soup.select("div.italic"))

"""Simple Case : Tags and ids"""
print(soup.select("div#Id"))


""" Parents and Children of a tag """

for ch in soup.find(class_="parent").children:
    print(ch)

for pa in soup.find("head").parents:
    print(pa)


""" Modifying the tags in the HTML"""

a = soup.find(class_ = "parent")
a.name = "span"

print(soup)


""" Modifying/Adding the class or any attribute or writing to the tag"""

a = soup.find(class_ = "parent")
a['class'] = "New Class"
a['text-align'] = "left"
a.string = "Hello dude"

print(soup)



""" Creating a new tag and writing to the tag"""

ulTag = soup.new_tag("ul")
liTag1 = soup.new_tag("li")
liTag2 = soup.new_tag("li")

liTag1['class'] = "new-list_item"
liTag2['class'] = "another-list_item"
liTag1.string = "Apples"
liTag2.string = "Magoes"

ulTag.append(liTag1)
ulTag.append(liTag2)

soup.html.body.insert(0,ulTag)
print(soup.prettify())
with open("Modified.html","w") as obj:
    obj.write(str(soup.prettify()))


""" Checking the attributes """

a = soup.find("div")
print(a.has_attr("class"))
print(a.has_attr("placeholder"))


