import random

print("Hashtag Randomiser\n")

'''
dick = {"hi" : "lol", "jo" : "loser", "wtf" : "whaidwhaf"}

for k, v in dick.items():
    print(k, v)
'''

def conv(x):
    
    realnum = 0
    if 'k' in x:
        if len(x) > 1:
            realnum = float(x.replace('k', '')) * 1000 # Convert k to a thousand
    elif 'm' in x:
        if len(x) > 1:
            realnum = float(x.replace('m', '')) * 1000000 # Convert m to a million
    elif 'b' in x:
        realnum = float(x.replace('b', '')) * 1000000000 # Convert b to a billion
    else:
        realnum = int(x) # Less than 1000

    return (int(realnum))

    #fin = ("{0:,}".format(int(realnum)))
    #return (fin.replace(",", " "))


while True:

    hashtags = {
    "#quoteoftheday" : "26.7m",
    "#qotd" : "14m",
    "#instaquote" : "10.1m",
    "#quotestoliveby" : "7.7m",
    "#quotestagram" : "4m",
    "#instaquotes" : "3.4m",
    "#quotesoftheday" : "3.3m",
    "#quotesdaily" : "1.8m",
    "#quotestags" : "1.7m",
    "#quotesofinstagram" : "1.2m",
    "#quotesgram" : "1.1m",
    "#thegoodquote" : "915k",
    "#quotesandsayings" : "776k",
    "#quotesforlife" : "694k",
    "#quoted" : "604k",
    "#quoteofthenight" : "339k",
    "#quotesforyou" : "318k",
    "#quotesaboutlifequotesandsayings" : "291k",
    "#quoteofday" : "253k",
    "#quotegram" : "244k",
    "#quotesoflife" : "216k",
    "#quotetoliveby" : "209k",
    "#quotedaily" : "174k",
    "#quotess" : "169k",
    "#quotestoinspire" : "141k",
    "#lovethisquote" : "138k",
    "#quoteme" : "123k",
    "#quotesilove" : "104k",
    "#quotesfordays" : "103k",
    "#quotes4you" : "100k",
    "#quotestoremember" : "96k",
    "#quotepage" : "92k",
    "#quotestag" : "86k",
    "#quotespage" : "85k",
    "#quoteslover" : "81k",
    "#quotelover" : "80k",
    "#quoteporn" : "77k",
    "#quotefortoday" : "60k",
    "#quotestoday" : "59k",
    "#quoteday" : "56k",
    "#quote_of_the_day" : "50k",
    "#quotelovers" : "46k",
    "#quotesforever" : "45.2k",
    "#quotesoninstagram" : "44.8k",
    "#quotesaccount" : "38.3k",
    "#instaquoteoftheday" : "25k",
    "#quotesworld" : "34k",
    "#instaquotesdaily" : "29k",
    "#quotestosee" : "28.8k",
    "#quotesabouteverything" : "28k",
    "#instaquotesgram" : "20k",
    "#quotestumblr" : "18.8k",
    "#quotesfortoday" : "14k ",
    "#quotesday" : "12.8k",
    "#quotestolive" : "12.7k",
    "#quotesilike" : "12.4k",
    "#quotes4u" : "11.8k",
    "#quotesaddict" : "11.4k",
    "#quotesforall" : "8.3k",
    "#quotesgraphy" : "7.3k",
    "#quoteswelove" : "5k",
    "#quoteshare" : "4.7k",
    "#quoteilike" : "2.9k",
    }

    newdict = {}


    while True:

        try:

            while True:
                    
                min_num = min(hashtags.items(), key=lambda x: conv(x[1])) 
                
                upr_limit = conv(input("\nI want my number to be at most (Lowest : " + min_num[1] + ") > "))
                
                if upr_limit < conv(min_num[1]):
                    print ("Please enter a limit higher than " + min_num[1])
                    continue
                else:
                    break
            
        except ValueError:
            print("Enter a number")
            continue

        break

            
    while True:
        
        try:

            while True:
                
                max_num = max(hashtags.items(), key=lambda x: conv(x[1]))
                
                low_limit = conv(input("\nI want my number to be at least (Highest : " + max_num[1] + ") > "))
                
                if low_limit > conv(max_num[1]):
                    print ("Please enter a limit lower than " + max_num[1])
                    continue
                else:
                    break
            
        except ValueError:
            print("Enter a number")
            continue

        break


    while True:
        
        try:

            h_num = input("\nHow many hashtags do you want? > ")
            break_loop = 0
            
            for i in range(int(h_num)):

                while True:
                    
                    randhash = random.choice(list(hashtags.items()))
                    #print(">>> " + randhash[0] + " : " + randhash[1])
                    break_loop += 1
                    #print (break_loop)

                    if break_loop > len(hashtags):
                        break
                    
                    if conv(randhash[1]) > low_limit and conv(randhash[1]) < upr_limit:
                        del hashtags[randhash[0]]
                        newdict[randhash[0]] = randhash[1]
                        break
                    else:
                        continue           

            if break_loop > len(hashtags):
                print ("There are all the available hashtags with that range\n")
                    
            for k, v in newdict.items():
                print(k, v)

            break

        except IndexError:
            print("Number cannot be more than the available hashtags")
            continue
            
        except ValueError:
            print("Enter a number")
            continue

        

        


'''
    try:
        quote = []
        h_num = input("\nHow many hashtags do you want? > ")
        for i in range(int(h_num)):
            chosen_hashtag = random.choice(hashtags)
            hashtags.remove(chosen_hashtag)
            quote.append(chosen_hashtag)
        print("")
        print(*quote, sep=' ')
        
    except IndexError:
        print("Number cannot be more than the available hashtags")
        
    except ValueError:
        print("Enter a number")
'''