from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import json
import datetime
import time

def start(update, context):
    update.message.reply_text("Welcome to busboi!")

def help(update, context):
    update.message.reply_text("Hewp!")

def message(update, context):
    start = time.time()
    header = {'AccountKey':'FP9dZIa6Tm6EsGeQWGRGOQ==', 'accept':'application/json'}

    busstopcode = update.message.text

    arrivalparam = {'BusStopCode':busstopcode}
    arrivaltarget = 'http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2'
    arrivalrequest = requests.get(arrivaltarget, params=arrivalparam, headers=header)
    arrivaljson = json.loads(arrivalrequest.text)

    if not len(arrivaljson["Services"]):
        update.message.reply_text("Please enter a valid busstop code!")
        return

    skiprange = [0 if int(busstopcode)//20//500*500+500*i < 0 else int(busstopcode)//20//500*500+500*i for i in range(-1,2)]
    def skipurl(skiprange):
        message = []
        for skip in skiprange:
            busstoptarget = f"http://datamall2.mytransport.sg/ltaodataservice/BusStops/?$skip={skip}"
            busstoprequest = requests.get(busstoptarget, headers=header)
            busstopjson = json.loads(busstoprequest.text)

            for stop in busstopjson["value"]:
                if busstopcode == stop["BusStopCode"]:
                    message.append(f"BUS STOP ({busstopcode})\n[{stop['Description']}]\nalong {stop['RoadName']}")
                    return message

    message = skipurl(skiprange)

    currenttime = datetime.datetime.now()
    nextbuses = ["NextBus", "NextBus2", "NextBus3"]

    message.append(f"{'-'*40}")
    for bus in range(len(arrivaljson['Services'])):
        message.append(f"Bus No. : {arrivaljson['Services'][bus]['ServiceNo']}\n")
        for nextbus in range(len(nextbuses)):
            try:
                arrival = (datetime.datetime.strptime(arrivaljson['Services'][bus][nextbuses[nextbus]]['EstimatedArrival'],'%Y-%m-%dT%H:%M:%S%z').replace(tzinfo=None)-currenttime).total_seconds()/60
                if arrival <= 0:
                    message.append(f"Next Bus ({nextbus+1}) = LEFT ({arrival*60:.3f} secs)")
                elif arrival <= 1:
                    message.append(f"Next Bus ({nextbus+1}) = ARRIVING ({arrival*60:.3f} secs)")
                else:
                    message.append(f"Next Bus ({nextbus+1}) = {arrival:.3f} mins")
            except:
                message.append(f"Next Bus ({nextbus+1}) = NA")
        message.append(f"{'-'*40}")

    message.append(f"Runtime : {round((time.time()-start),3)}s")
    update.message.reply_text("\n".join(message))

def main():
    updater = Updater("755655363:AAHfOKX-tIUy8xwP0HsH-H9rrUVGnraVfzI", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, message))
    #dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()