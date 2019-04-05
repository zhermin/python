import time
from src.pillowtalk import CreatePost
from src.hashbrowns import RandomCaption
from src.adamantium import ShareInstaPost

# TODO : settle padding below each line for scraped quote
# TODO : write failsafe for pillowtalk.py scrapeText()
# TODO : do a while, try/except loop to make sure AT LEAST one quote is scraped from either eduro/brainyquote/ownfile(?)

starttime = time.time()

print("[INITIALIZED PYSTABOT]\n")
myPost = CreatePost().saveImg()
myCaption = RandomCaption().getCaption()
ShareInstaPost("antivnti", "anti//vnti", myCaption, myPost).sharePost()
print("\n[PYSTABOT TERMINATED]")

print("{} seconds".format(time.time() - starttime))