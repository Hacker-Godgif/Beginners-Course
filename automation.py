#Please do not copy x path of driver you please go and copy your webbrowser xpath
#Download Chromedriver also Search on google Download Google chrome selenium driver

import pyttsx3
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import os
os.chdir("Put your file or folder location of where you put this automation file")

#Speaking Functions
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 150)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

opt = Options()
opt.add_argument("start-maximized")
opt.add_argument("==disable-extensions")
            # Pass the arguement 1 to allow and 2 to block
opt.add_experimental_option("prefs", {\
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
})
driver = webdriver.Chrome(chrome_options=opt, executable_path='E://chromedriver_win32//chromedriver.exe')
driver.get('https://accounts.google.com/signin/v2/identifier?service=classroom&continue=https%3A%2F%2Fclassroom.google.com%2F&flowName=GlifWebSignIn&flowEntry=AddSession')
Username = driver.find_element_by_xpath('//*[@id="identifierId"]')
Username.click()
Username.send_keys('Enter you email here')
speak("Email has entered Sucessfully")
Next = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
Next.click()
time.sleep(5)
Password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
Password.click()
Password.send_keys('Enter your password here')
speak("Password has enterd sucessfully")
Next1 = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
Next1.click()
speak("Entered in Classroom")
time.sleep(5)
            # after joining the classrom the functions is now working
classroom = driver.find_element_by_xpath('//*[@id="yDmH0d"]')
classroom.click()
time.sleep(5)
            #Subject Information
SSC = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div/div[2]/div/ol/li[4]/div[1]/div[3]/h2/a[1]/div[1]')
SSC.click()
speak("Entered SSC class")
time.sleep(5)
            #Join meeting link
ssc_meeting = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/span/a/div')
ssc_meeting.click()
speak("Click on link for attending class")
#Switches the tab
current_tab=driver.window_handles[1]
driver.switch_to_window(current_tab)

#Switch of mic and cam
mic = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[6]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div')
mic.click()
speak("Microphone has turned off successfully")
time.sleep(5)
cam = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[6]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div[4]/div[2]/div/div')
cam.click()
speak("Camera has been turned off successfully")
time.sleep(5)
#Join Class
join = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[6]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span')
join.click()
speak("Meeting joined successfully")
