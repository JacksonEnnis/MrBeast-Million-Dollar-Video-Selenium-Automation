from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time


email = input("What is your email?\n")
password = input("What is your password? \n")
EXE_PATH = r'C:\Users\Arcti\Desktop\sel_stuff\chromedriver'

driver = webdriver.Chrome(executable_path=EXE_PATH)

driver.get("https://accounts.google.com/signin/v2/identifier?hl=en&service=youtube&uilel=3&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Fhl%3Den%26next%3D%252Faccount%26feature%3Dredirect_login%26app%3Ddesktop%26action_handle_signin%3Dtrue&passive=true&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

driver.find_element_by_id("identifierId").send_keys(email)
driver.find_element_by_id("identifierNext").click()

time.sleep(1)
driver.find_elements_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")[0].send_keys(password)

driver.find_element_by_id("passwordNext").click()

time.sleep(2)

channel = "https://www.youtube.com/user/MrBeast6000/videos"
#'https://www.youtube.com/user/MrBeast6000/videos'
#
driver.get(channel)

firstVideoTitle = driver.find_element_by_id("video-title")
titles = driver.find_elements_by_xpath("//*[@id='video-title']")

latestVideoTitle = titles[0].text

#Last To Stop Biking Wins $1,000,000 (Part 4)
while(latestVideoTitle == "Last To Stop Biking Wins $1,000,000 (Part 4)"):
    try:
        time.sleep(1)
        #https://www.youtube.com/channel/UCedzZUSpNc8QjGZUIV0K9rg
        driver.get(channel)
        #now you can refresh the page!
        driver.refresh()
        
        titles = driver.find_elements_by_xpath("//*[@id='video-title']")
        latestVideoTitle = titles[0].text
        print("CAUGHT IN INFINITY")
        
    except:
        print("A little too fast")
        
videos = driver.find_elements_by_xpath("//*[@id='thumbnail']")

videos[0].click()

isScrolled = False
while isScrolled == False:
    try:
        time.sleep(2.3)
        driver.find_element_by_tag_name('body').send_keys(Keys.END) # Use send_keys(Keys.HOME) to scroll up to the top of page
        isScrolled = True
    except:
        print("OUCH")
        pass

mSent = False
while mSent == False:
    try:
        comments = driver.find_element_by_id("placeholder-area").click()
        driver.find_element_by_id("contenteditable-root").send_keys("SHOP MR BEAST")
        driver.find_element_by_id("submit-button").click()
        mSent = True
    except:
        pass