from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

my_url = "https://sg.carousell.com/search/products/?query=magnum%20boots"
req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
urlopen(req).close()
page_soup = soup(webpage, "html.parser")

[s.decompose() for s in page_soup('script')]


containers = page_soup.findAll("div", {"class":"col-lg-3 col-md-4 col-sm-4 col-xs-6"})



filename = "magnum.csv"
f = open(filename, "w")

headers = "No., Product Name, Price, Details, Posted, Username\n"

f.write(headers)


x = 1

for container in containers:

	product_name = container.findAll("div", {"class":"aj-m"})[0].text
	product_name = ''.join(c for c in product_name if c <= '\uFFFF')

	price = container.findAll("div", {"class":"aj-k"})[0].findChildren()[0].text
	price = ''.join([i for i in price if i.isdigit()])

	size = container.findAll("div", {"class":"aj-k"})[0].findChildren()[1].text
	time_posted = container.span.text
	username = container.findAll("div", {"class":"aj-B"})[0].text
	
	print("ITEM " + str(x))
	print("Product Name : " + product_name)
	print("Price : $" + price)
	print("Details : " + size)
	print("Time Posted : " + time_posted)
	print("Username : " + username)
	print("\n")
	
	f.write(str(x) + ", " + str(product_name.replace(",", "|")) + ", " + str(price) + ", " + str(size.replace(",", "|")) + ", " + str(time_posted) + ", " + str(username) + "\n")

	x += 1

f.close()
