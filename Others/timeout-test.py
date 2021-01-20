import time

class udumb():

    def __init__(self):
        
        self.trythis()
        print("end")
    
    def trythis(self):

        self.cd = 0
        while True:
            try:
                self.one()
                self.two()
                self.three()
                break
            except:
                print("RESTARTING")
                self.cd = 0
                continue

    def one(self):
        while True:
            if self.cd == 5:
                print("success 1")
                self.cd = 0
                return
            else:
                if self.cd == 10:
                    print("timeout 1")
                    raise Exception
                else:
                    print("trying 1..")
                    time.sleep(.5)
                    self.cd += 1

    def two(self):
        while True:
            if self.cd == 7:
                print("success 2")
                self.cd = 0
                return
            else:
                if self.cd == 10:
                    print("timeout 2")
                    raise Exception
                else:
                    print("trying 2..")
                    time.sleep(.5)
                    self.cd += 1

    def three(self):
        while True:
            if self.cd == 13:
                print("success 3")
                self.cd = 0
                return
            else:
                if self.cd == 10:
                    print("timeout 3")
                    raise Exception
                else:
                    print("trying 3..")
                    time.sleep(.5)
                    self.cd += 1

udumb()