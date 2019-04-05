import textwrap, os
from PIL import Image, ImageDraw, ImageFont
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

class CreatePost:
    
    def __init__(self): # initialise landscape [0] / portrait [1]

        self.postFolder = f"{os.getcwd()}\\posts\\"
        self.totalPost = len(os.listdir(self.postFolder))
        self.num = self.totalPost % 2
        print(f"[POST {self.totalPost+1}]")

        self.fileName = f"{self.postFolder}instapost_{self.totalPost+1}.jpg"

        self.winW = self.winH = 1000
        self.whitespace = 75
        self.colors = [(240,240,240), (40,40,40)]
       
        if self.num == 0: # PORTRAIT
            self.bgColor = self.colors[self.num+1]
            self.accentColor = self.colors[self.num]
            print("The New Post will be in Portrait Mode..")
        else: # LANDSCAPE
            self.bgColor = self.colors[self.num-1]
            self.accentColor = self.colors[self.num]
            print("The New Post will be in Landscape Mode..")

        self.img = Image.new("RGB", (self.winW,self.winH), color=self.bgColor)
        self.draw = ImageDraw.Draw(self.img)

    def scrapeText(self): # scrape quote & author from web

        self.quote = "\"I do not know how to teach philosophy without becoming a disturber of established religion.\""
        self.author = "Thomas Jefferson".upper()

        # quote_url = "https://www.eduro.com/"
        # req = Request(quote_url, headers={'User-Agent': 'Mozilla/5.0'})
        # page_html = urlopen(req).read()
        # urlopen(req).close()
        # page_soup = soup(page_html, "html.parser")

        # all_dailyquotes = page_soup.findAll("dailyquote")
        # self.quote = "\"{}\"".format(all_dailyquotes[0].findAll("p")[0].text)
        # self.author = all_dailyquotes[0].findAll("p")[1].text[4:].strip().upper()

        # brainyquote = page_soup.findAll("img")[0].get("alt")

    def writeQuote(self): # draw quote text

        quotewrap = textwrap.wrap(self.quote, width=30)
        quotewrap.append("\n")
        quotewrap.append("\n")

        if len(self.quote) > 110:
            quotefontsize = 45
        else:
            quotefontsize = 55

        quotefont = ImageFont.truetype("BELLI.TTF", quotefontsize)
        w,h = quotefont.getsize(self.quote)
        h *= (len(quotewrap))
        current_h, padding = (self.winH/2 - h/2), 20
        # to push down the first line because for some reason the first line is lower than the other lines
        weirdspace = 0

        for line in quotewrap:
            w,h = quotefont.getsize(line)
            self.draw.text( ((self.winW/2 - w/2), current_h - weirdspace), line, font=quotefont, fill=self.accentColor)
            current_h += h + padding
            weirdspace = 0

    def drawDash(self): # draw dash

        dash = 80
        self.draw.rectangle([self.winW/2-dash/2, self.winH-275, self.winW/2-dash/2+dash, self.winH-275+3], fill=self.accentColor)

    def writeAuthor(self): # draw author text

        authorfont = ImageFont.truetype("REFSAN.TTF", 24)
        w,h = authorfont.getsize(self.author)
        self.draw.text(((self.winW/2 - w/2), (self.winH - 200)), self.author, font=authorfont, fill=self.accentColor)

    def drawWhitespace(self): # draw whitespace & border

        border = 50
        if self.num == 0: # PORTRAIT
            self.draw.rectangle([0,0,self.whitespace,self.winH], fill=(255,255,255))
            self.draw.rectangle([self.winW-self.whitespace,0,self.winW,self.winH], fill=(255,255,255))

            self.draw.rectangle([border+self.whitespace,border,self.winW-border-self.whitespace,self.winH-border], width=3, outline=self.accentColor)
        else: # LANDSCAPE
            self.draw.rectangle([0,0,self.winW,self.whitespace], fill=(255,255,255))
            self.draw.rectangle([0,self.winH-self.whitespace,self.winW,self.winH], fill=(255,255,255))

            self.draw.rectangle([border,border+self.whitespace,self.winW-border,self.winH-border-self.whitespace], width=3, outline=self.accentColor)

    def drawEverything(self):

        print("Scraping Quote of the Day from the Internet..")
        self.scrapeText()
        print("Drawing the texts and dash and whitespaces onto the Image..")
        self.writeQuote()
        self.drawDash()
        self.writeAuthor()
        self.drawWhitespace()

    def showImg(self): # display drawn image without saving

        self.drawEverything()
        self.img.show()

    def saveImg(self): # save drawn image in the postFolder directory

        self.drawEverything()
        print(f"Saving the Image as [instapost_{self.totalPost+1}.jpg]..")
        self.img.save(self.fileName)

        return self.fileName

if __name__ == "__main__":

    CreatePost().showImg()

    # for i in range(2):
    #     CreatePost().saveImg()


# import requests

# proxies = {"http": "http://52.163.207.100:3128",
#                 "https": "http://52.163.207.100:3128"}

# quote_url = "https://www.eduro.com/"
# req = requests.get(quote_url, headers={'User-Agent': 'Mozilla/5.0'}, proxies=proxies)
# page_html = req.content
# req.close()
# page_soup = soup(page_html, "html.parser")