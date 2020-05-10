# run using the folowing command to ignore the warning messages
# python -W ignore run.py 218925122310 3 1
# pre req.
#pip install selenium
#brew cask upgrade chromedriver
import sys
import time
#####################
#####################
phone=int(sys.argv[1]) #218925122310
add=int(sys.argv[2]) #3
inc=int(sys.argv[3]) #1
#####################
#####################
from selenium import webdriver 
from time import sleep 
p=""
i=0
from selenium.webdriver.chrome.options import Options  
options = webdriver.ChromeOptions()
options.add_argument("--headless")  
options.add_argument('window-size=1200x600')

f = open("list.csv", "a")
driver = webdriver.Chrome(chrome_options=options) 
sleep(1) 
for i in range(0,add*inc,inc):
    t1 = time.time()
    u="+"+str(phone+i)
    driver.get('https://www.facebook.com/') 
    #print ("Opened facebook") 
    sleep(1) 
    username_box = driver.find_element_by_id('email') 
    username_box.send_keys(u) 
    #print ("Email Id entered=",u) 
    sleep(1) 
    password_box = driver.find_element_by_id('pass') 
    password_box.send_keys(p) 
    #print ("Password entered=",p) 
    login_box = driver.find_element_by_id('loginbutton') 
    login_box.click() 
    sleep(1) 
    x=driver.find_element_by_css_selector('div._4rbf')
    ###sleep(1) 
    y=x.get_attribute('innerHTML')
    a=0
    if "The password you’ve entered is incorrect." in y:
        r=u+" [found] "
        a=1
    if "The email or phone number you’ve entered doesn’t match any account." in y or "The phone number you’ve entered doesn’t match any account." in y:
        r=u+" [not found] "
        a=2
    if a==0:
        r=u+" [Unknown] "
    t2 = time.time()
    r=r+"- "+str(round(t2-t1,1))
    print(r)
    if a==1:
        f.write(u+"\n")
driver.quit() 
f.close()
r=""



