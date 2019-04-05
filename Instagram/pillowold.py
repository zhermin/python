from PIL import Image, ImageDraw, ImageFont
import textwrap
#FRSCRIPT.TTF

def portrait():
    winW = 1080
    winH = 1350
    bgColor = (40,40,40)
    accentColor = (200,200,200)

    img = Image.new("RGB", (winW,winH), color=bgColor)

    quote = "\"I do not know how to teach philosophy without becoming a disturber of established religion.\""
    quotewrap = textwrap.wrap(quote, width=30)
    quotewrap.append("\n")
    quotewrap.append("\n")

    if len(quote) > 110:
        quotefontsize = 50
    else:
        quotefontsize = 60

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
    draw.text(((winW/2 - w/2), (winH - 200)), author, font=authorfont, fill=accentColor)

    whitespace = 70
    draw.rectangle([0,0,whitespace,winH], fill=(255,255,255))
    draw.rectangle([winW-whitespace,0,winW,winH], fill=(255,255,255))

    border = 50
    draw.rectangle([border+whitespace,border,winW-border-whitespace,winH-border], width=3, outline=accentColor)

    img.show()


def landscape():
    winW = winH = 1080
    bgColor = (200,200,200)
    accentColor = (40,40,40)

    img = Image.new("RGB", (winW,winH), color=bgColor)

    quote = "\"I do not know how to teach philosophy without becoming a disturber of established religion.\""
    quotewrap = textwrap.wrap(quote, width=30)
    quotewrap.append("\n")
    quotewrap.append("\n")

    if len(quote) > 110:
        quotefontsize = 50
    else:
        quotefontsize = 60

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
    draw.text(((winW/2 - w/2), (winH - 200)), author, font=authorfont, fill=accentColor)

    whitespace = 75
    draw.rectangle([0,0,winW,whitespace], fill=(255,255,255))
    draw.rectangle([0,winH-whitespace,winW,winH], fill=(255,255,255))

    border = 50
    draw.rectangle([border,border+whitespace,winW-border,winH-border-whitespace], width=3, outline=accentColor)

    img.show()


orderList = [1,2]

for order in range(len(orderList)):

    index = orderList[order] % 2

    if index == 0:
        # winW = winH = 1080
        landscape()
    else:
        # winW = 1080
        # winH = 1350
        portrait()
        
    #drawImg(index)









#def drawImg(index):

    # colors = [(200,200,200), (40,40,40)]
    # bgColor = colors[index]
    # accentColor = colors[index-1]
        
    # img = Image.new('RGB', (winW,winH), color=bgColor)

    #quote = "\"When you reach the end of your rope, tie a knot in it and hang on.\""
    # quote = "\"I do not know how to teach philosophy without becoming a disturber of established religion.\""
    # quotewrap = textwrap.wrap(quote, width=30)
    # quotewrap.append("\n")
    # quotewrap.append("\n")
    #print(len(quote))

    # if len(quote) > 110:
    #     quotefontsize = 50
    # else:
    #     quotefontsize = 60

    # #FRSCRIPT.TTF
    # quotefont = ImageFont.truetype("BELLI.TTF", quotefontsize)
    # w,h = quotefont.getsize(quote)
    # h *= (len(quotewrap))
    # current_h, padding = (winH/2 - h/2), 10

    # draw = ImageDraw.Draw(img)

    # for line in quotewrap:
    #     w,h = quotefont.getsize(line)
    #     draw.text( ((winW/2 - w/2), current_h), line, font=quotefont, fill=accentColor)
    #     current_h += h + padding

    # dash = 80
    # draw.rectangle([winW/2-dash/2, winH-300, winW/2-dash/2+dash, winH-300+3], fill=accentColor)

    # author = "Thomas Jefferson".upper()
    # authorfont = ImageFont.truetype("REFSAN.TTF", 28)
    # w,h = authorfont.getsize(author)
    # draw.text( ((winW/2 - w/2), winH - 200),author , font=authorfont, fill=accentColor)

    # leftrightspace = topbotspace = 0
    # if index == 1:
    #     leftrightspace = 70
    #     draw.rectangle([0,0,leftrightspace,winH], fill=(255,255,255))
    #     draw.rectangle([winW-leftrightspace,0,winW,winH], fill=(255,255,255))
    # else:
    #     topbotspace = 75
    #     draw.rectangle([0,0,winW,topbotspace], fill=(255,255,255))
    #     draw.rectangle([0,winH-topbotspace,winW,winH], fill=(255,255,255))

    # border = 50
    # draw.rectangle([border+leftrightspace,border+topbotspace,winW-border-leftrightspace,winH-border-topbotspace], width=3, outline=accentColor)

    # img.show()
    #img.save("pillowtalk.png")

    
