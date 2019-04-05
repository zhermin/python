from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

quote_url = "https://www.eduro.com/"
req = Request(quote_url, headers={'User-Agent': 'Mozilla/5.0'})
page_html = urlopen(req).read()
urlopen(req).close()
page_soup = soup(page_html, "html.parser")

all_dailyquotes = page_soup.findAll("dailyquote")
dailyquote = all_dailyquotes[0].findAll("p")[0].text
dailyauthor = all_dailyquotes[0].findAll("p")[1].text[4:].strip()

print(dailyquote + "\n" + dailyauthor)
input()

#dailyquote = page_soup.findAll("img")[0].get("alt")