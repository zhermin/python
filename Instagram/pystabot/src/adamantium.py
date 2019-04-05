import datetime, time, pyautogui, pyperclip, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

pyautogui.failsafe = True # Force Quit at Top Left Corner with Cursor

class ShareInstaPost:

    def __init__(self, profilename, mypassword, hashtags, filename):

        self.dirFolder = os.getcwd()

        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument("--headless")
        chrome_options.add_argument("incognito")
        chrome_options.add_argument('--user-agent="Mozilla/5.0 (Linux; Android 9; SM-G955F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.90 Mobile Safari/537.36"')
        self.driver = webdriver.Chrome(f"{self.dirFolder}\\src\\chromedriver.exe", options=chrome_options)

        self.driver.set_window_position(-2000,0)

        self.profilename = profilename
        self.mypassword = mypassword
        self.hashtags = hashtags
        self.filename = filename

    def homePage(self):

        print("Accessing Instagram..")
        self.driver.get("https://instagram.com/")

        login = None
        while not login:
            try:
                print("Trying to find Login Button..")
                login = self.driver.find_element_by_link_text("Log in")
                print("FOUND LOGIN BUTTON")
                login.click()
            except:
                continue

    def loginPage(self):

        usernamebtn = passwordbtn = None
        while not usernamebtn or not passwordbtn:
            try:
                print("Trying to find Username/Password Fields..")
                usernamebtn = self.driver.find_element_by_name("username")
                passwordbtn = self.driver.find_element_by_name("password")
                print("FOUND USERNAME/PASSWORD FIELDS")
                usernamebtn.send_keys(self.profilename)
                passwordbtn.send_keys(self.mypassword)
                passwordbtn.send_keys(Keys.ENTER)
                
                loginURL = self.driver.current_url
                while self.driver.current_url == loginURL:
                    try:
                        time.sleep(2)
                        passwordbtn = self.driver.find_element_by_name("password")
                        print("WRONG PASSWORD")
                        continue
                    except:
                        print("PASSWORD ACCEPTED")
                        print("Logging In..")
                        break

            except:
                time.sleep(1)
                continue

    def newInstaPost(self):

        print("Redirecting to Profile Page..")
        self.driver.get(f"https://instagram.com/{self.profilename}/")

        newpostbtn = None
        while not newpostbtn:
            try:
                print("Waiting for Page to Load..")
                newpostbtn = self.driver.find_element_by_xpath("//span[@aria-label='New Post']")
                print("PROFILE PAGE LOADED")
                print("FOUND THE NEW POST BUTTON")
                newpostbtn.click()
            except:    
                time.sleep(2)
                continue

    def uploadPost(self):

        postnextbtn = None
        while not postnextbtn:
            try:
                postnextbtn = self.driver.find_element_by_xpath("//button[contains(text(), 'Next')]")
                print("FILE UPLOADED SUCCESSFULLY")
                print("FOUND THE NEXT BUTTON")
                postnextbtn.click()
            except:
                print("Trying to Upload the File, make sure the Window is in Focus..")
                time.sleep(1)
                pyautogui.typewrite(self.filename)
                pyautogui.press('enter')
                time.sleep(.5)
                continue

    def writeCaption(self):

        captionbtn = None
        now = datetime.datetime.now().strftime("%H%M%S%d%m%y")

        fullCaption = f"[{now}]\n"
        fullCaption += "-\n"
        fullCaption += "@VYBS.vtg\n"
        fullCaption += "-\n"*5
        fullCaption += self.hashtags
        pyperclip.copy(fullCaption)

        while not captionbtn:
            try:
                print("Trying to find Caption textbox..")
                captionbtn = self.driver.find_element_by_tag_name("textarea")
                print("FOUND THE CAPTION TEXTBOX")
                captionbtn.send_keys(Keys.CONTROL, "v")
                print("Preparing to Post..")
            except:
                continue

    def postMockup(self):
        
        self.homePage()
        self.loginPage()
        self.newInstaPost()
        self.uploadPost()
        self.writeCaption()

    def sharePost(self):

        self.postMockup()
        
        postsharebtn = None
        while not postsharebtn:
            try:
                print("Trying to find the Share button..")
                postsharebtn = self.driver.find_element_by_xpath("//button[contains(text(), 'Share')]")
                print("FOUND THE SHARE BUTTON")
                sharepageURL = self.driver.current_url
                postsharebtn.click()
            except:
                continue

        while True:
            if self.driver.current_url == sharepageURL:
                print("Posting to Instagram..")
                time.sleep(1)
                continue
            else:
                print("POST SHARED SUCCESSFULLY")
                break

        print("Shutting Down Browser..")
        self.driver.quit()
        print("CODE SELF-DESTRUCTED")

if __name__ == "__main__":
    ShareInstaPost("antivnti", "anti//vnti", None, None).postMockup()
    input()