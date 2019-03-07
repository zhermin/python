from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class":"item-container"})


filename = "products.csv"
f = open(filename, "w")

headers = "Brand, Name, Shipping\n"

f.write(headers)

for container in containers:

	brand = container.a.img["alt"].split(" ")[0]
	name = container.a.img["alt"]
	shipping = container.findAll("li", {"class":"price-ship"})[0].text.strip()


	print("Brand : " + brand)
	print("Name : " + name)
	print("Shipping : " + shipping + "\n")

	f.write(brand + ", " + name.replace(",", "|") + ", " + shipping + "\n")

f.close()	