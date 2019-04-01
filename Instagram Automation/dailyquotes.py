import pyautogui, datetime, time, os, random
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

now = datetime.datetime.now().strftime("%H%M%S%d%m%y")
print(now)
input()




# 1914190104
# 1405190105
# 0054190106
# 0708190107
# 1204190108
# 1631190109
# 2109190110
# 1155190111
# 2349190112

# 1914040119
# 1405050119
# 0054060119
# 0708070119
# 1204080119
# 1631090119
# 2109100119
# 1155110119
# 2349120119