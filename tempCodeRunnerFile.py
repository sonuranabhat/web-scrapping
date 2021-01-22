for link in anchors:
    if(link.get('href')!='#'):
        linkText="https://codewithharry.com" +link.get('href')
        all_links.add(linkText)
        print(linkText)