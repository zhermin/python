import pyautogui, time, os, random

os.startfile("C:\Program Files\Open Media LLC\combin\combin.exe")
time.sleep(5)

pyautogui.failsafe = True # Force Quit at Top Left Corner with Cursor

# print(pyautogui.size())

hashtags = [
"#poetryofinstagram",
"#poetryporn",
"#poetsociety",
"#poetryofig",
"#igpoetry",
"#poetrygram",
"#poetryinmotion",
"#poetrylovers",
"#poetrysociety",
"#poetryslam",
"#micropoetry",
"#typewriterpoetry",
"#lovepoetry",
"#poetryislife",
"#omypoetry",
"#poetrycommunityofinstagram",
"#poetrybook",
"#poetrylove",
"#poetry_addicts",
"#sadpoetry",
"#poetryhive",
"#poetrylover",
"#poetryisart",
"#poetrytribe",
"#poetryislove",
"#poetryclub",
"#poetrybooks",
"#poetrycorner",
"#poetryloving",
"#poetryoftheday",
"#poetryaddict",
"#poetryforthesoul",
"#poetrydaily"
]


user = [
"yuli_quotes"
]


pyautogui.click(200, 45, duration = 0.25) # Tools Tab
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('enter') # Preferences Options
pyautogui.click(865, 360, duration = 0.25) # Activities Tab
pyautogui.click(1030, 540, duration = 0.25) # Like Last Dropdown Menu
pyautogui.click(1030, 610, duration = 0.25) # 3 Posts Option
pyautogui.press('esc')


for i in range(7):
	
	randhash = random.choice(hashtags) # Choose a random Hashtag
	hashtags.remove(randhash) # Remove chosen Hashtag
	pyautogui.click(90, 180, duration = 0.25) # Search Button
	pyautogui.click(280, 90, duration = 0.25) # Add Search Button
	pyautogui.click(1160, 655, duration = 0.5) # Analyze User Button
	pyautogui.typewrite(randhash, interval = 0.1) # Type Hashtag
	pyautogui.press('enter')

for i in range(1):
	
	randuser = random.choice(user) # Choose a random User
	user.remove(randuser) # Remove chosen User
	pyautogui.click(90, 180, duration = 0.25) # Search Button
	pyautogui.click(280, 90, duration = 0.25) # Add Search Button
	pyautogui.click(1120, 375, duration = 0.5) # Users Button
	pyautogui.click(1160, 655, duration = 0.25) # User Active Button
	pyautogui.typewrite(randuser, interval = 0.1) # Type Username
	time.sleep(2)
	pyautogui.click(990, 530, duration = 0.25) # Correct User
	pyautogui.press('enter')
	
	
time.sleep(300) # 5 mins
os.startfile("C:\Program Files\Open Media LLC\combin\combin.exe")

for i in range(1): # User Follow + Like Last 3
	pyautogui.click(480, 145, duration = 0.5) # Follow Button
	pyautogui.press('enter')
	pyautogui.click(410, 140, duration = 0.5) # Like Last Few Posts Button
	pyautogui.press('enter')	
	pyautogui.press('tab')
	pyautogui.press('down')
	
for i in range(7): # Like All from Hashtag
	pyautogui.click(410, 140, duration = 0.5) # Like Posts Button
	pyautogui.press('enter')
	pyautogui.press('tab')
	pyautogui.press('down')