from urllib.request import Request, urlopen
import urllib.request
from bs4 import BeautifulSoup as soup
from pathlib import Path
import os

url = str(input('URL: '))
dirName = str(input('Ordner: '))

os.mkdir(dirName)

req = Request(url, headers={'User-Agent': 'Mozilla'})
webpage = urlopen(req).read()
page_soup = soup(webpage, 'lxml')
images = page_soup.find_all('meta', property="og:image")
links = []

for image in images:
    link = image.get('content')
    links.append(link)

print('Images detected! ' + str(len(links)))

for i in range(len(links)):
    path = Path(__file__).parent.absolute()
    filepath = str(path) + '\\' + dirName + '\\'
    filename = 'img{}.jpg'.format(i)
    fullfilename = filepath + filename
    urllib.request.urlretrieve(links[i], fullfilename)
    
print('Done!')