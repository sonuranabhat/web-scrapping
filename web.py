#Step 0: install all the requirements
#pip install requests
#pip install bs4
#pip install html5lib
import requests
from bs4 import BeautifulSoup
url="https://www.codewithharry.com"
#Step1:Get the HTML
r=requests.get(url)
htmlContent=r.content
#print(htmlContent)


#Step2:Parse the HTML
soup=BeautifulSoup(htmlContent,'html.parser')
#print(soup.prettify)


#step 3: HTML Tree Traversal
#commonly used types of objects
#1.tags/2.navigablestring/3.beautifulsoup/4.comment
'''print(type(soup))
print(type(title))
print(type(title.string)) '''

#get the tiltle of html page
#title=soup.title

#get all the paragraphs from the page
'''para=soup.find_all('p')
print(para)'''
#get all the anchors tag from the page
anchors=soup.find_all('a')
all_links=set()
#print(anchors)
#get all the links from the page
'''for link in anchors:
    if(link.get('href')!='#'):
        linkText="https://codewithharry.com" +link.get('href')
        all_links.add(linkText)
        print(linkText)'''

#print(soup.find('p'))#finds first element from html page
#print(soup.find('p')['class'])#gets classes/id of any element from page

#print(soup.find_all("p",class_="lead"))

#get the text from the tags/soup
'''print(soup.find('p').get_text())
print(soup.get_text())'''


'''markup="<p><!--this is comment--></p>"
soup2=BeautifulSoup(markup)
print(soup2.p)
print(soup2.p.string)
print(type(soup2.p.string))

exit()'''

navbarSupportedContent=soup.find(id='navbarSupportedContent')
#.contents=a tag's children are available as a list
#.children=a tag's children are available as a generator


'''for ele in navbarSupportedContent.contents:
    print(ele)
for ele in navbarSupportedContent.children:
    print(ele)


for elements in navbarSupportedContent.strings:
    print(elements)
for elements in navbarSupportedContent.stripped_strings:
    print(elements)

print(navbarSupportedContent.parent)
#print(navbarSupportedContent.parents)-.parents then you can iterate
for item in navbarSupportedContent.parents:
    print(item.name)
'''
#next sibling or previous sibling
print(navbarSupportedContent.next_sibling.next_sibling)
#it shows blank 

print(navbarSupportedContent.next_sibling.next_sibling)
#it shows none

print(navbarSupportedContent.previous_sibling.previous_sibling)
#new line is also considered previous siblings so

e=soup.select('#loginModal')
print(e)
e=soup.select('.modal-footer')
print(e)




 