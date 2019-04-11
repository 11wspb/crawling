
import urllib 
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url = 'https://www.wartaekonomi.co.id/read223367/grab-incar-bidang-travel-dan-kesehatan.html'
uClient = uReq(url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
containers =  page_soup.findAll("div", {"class":"news-post"})

file_name = "data.txt"
f = open(file_name, "w")

header =  "sumber: "+ url + "\n"

f.write(header)

for container in containers:
    judulb = container.findAll("h2", {"class":"'title-large"})
    judul = judulb[0].text
    
    isib = container.findAll("div", {"class":"news-post-content clearfix"})
    isi = isib[0].text
    
    print("Judul : "+ judul)
    print("Isi : "+ isi)
    
    f.write("Judul : "+ judul + "\n" + "Isi : "+ isi + "\n")
    
f.close()