import requests  #allows you to request data from a webpage
from bs4 import BeautifulSoup
def crawl(max_pages):
    pages = 1
    while pages <= max_pages:
        url = "https://www.livingwordmedia.org/old/process.php?geturl=424"
        source_code = requests.get(url)
        plain_text = source_code.text #text the text without the headers and shit
        soup = BeautifulSoup(plain_text,features="html.parser")
        for link in soup.findAll('div',{'class': "col-md-9 col-sm-6"}):
            href = link.get('href')
            title = link.string#to getbthe atring in it
            return print(href)
            return print(title)
        pages +=1
    

crawl(5)