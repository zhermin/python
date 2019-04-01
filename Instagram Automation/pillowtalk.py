from PIL import Image, ImageDraw, ImageFont
import textwrap

#quote = "\"When you reach the end of your rope, tie a knot in it and hang on.\""
quote = "\"I do not know how to teach philosophy without becoming a disturber of established religion.\""
quotewrap = textwrap.wrap(quote, width=30)
quotewrap.append("\n")
quotewrap.append("\n")
#print(len(quote))

if len(quote) > 110:
    quotefontsize = 60
else:
    quotefontsize = 72

def drawImg(bgColor, accentColor):
        
    img = Image.new('RGBA', (winW,winH), color=bgColor)

    #FRSCRIPT.TTF
    quotefont = ImageFont.truetype("BELLI.TTF", quotefontsize)
    w,h = quotefont.getsize(quote)
    h *= (len(quotewrap))
    current_h, padding = (winH/2 - h/2), 10

    draw = ImageDraw.Draw(img)

    for line in quotewrap:
        w,h = quotefont.getsize(line)
        draw.text( ((winW/2 - w/2), current_h), line, font=quotefont, fill=accentColor)
        current_h += h + padding

    dash = 80
    draw.rectangle([winW/2-dash/2, winH-300, winW/2-dash/2+dash, winH-300+3], fill=accentColor)

    author = "Thomas Jefferson".upper()
    authorfont = ImageFont.truetype("REFSAN.TTF", 28)
    w,h = authorfont.getsize(author)
    draw.text( ((winW/2 - w/2), winH - 200),author , font=authorfont, fill=accentColor)

    draw.rectangle([50,50,winW-50,winH-50], width=3, outline=accentColor)

    img.show()
    #img.save("pillowtalk.png")

    
orderList = [1]
colors = [(250,250,250), (40,40,40)]

for order in range(len(orderList)):

    index = orderList[order] % 2

    if index == 0:
        winW = winH = 1080
    else:
        winW = 1080
        winH = 1350

    drawImg(colors[index], colors[index-1])