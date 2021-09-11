# Coursera Professional Certification and Specialization Data collection
from selenium import webdriver
import time
import pandas as pd
import re

option = webdriver.ChromeOptions() # setting up in a way that chrome wont open
option.add_argument('--start-maximized')

web = webdriver.Chrome(options=option)
web.get('https://www.coursera.org/in?authMode=login')  ## coursea website

time.sleep(3)




web.find_element_by_xpath('//*[@id="email"]').send_keys('EMAILID')  # your email
web.find_element_by_xpath('//*[@id="password"]').send_keys('PASSWORD')  # your password
time.sleep(2)
web.find_element_by_xpath('/html/body/div[3]/div/div/section/section/div[1]/form/button').click()

humanverification = input('CLICK ENTER AFTER YOU CLEAR CAPTCHA')  # you will have to clear captcha verification and click enter

web.find_element_by_xpath('//*[@id="rendered-content"]/div/div/div/span/div[1]/header/div[2]/div/div[1]/div/div/div[3]/div/div[2]/form/div/div/div[1]/button[2]/div').click() #  login button
time.sleep(4)

web.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/span').click() # selecting 'english'
web.find_element_by_xpath('//*[@id="react-select-2--option-0"]/div/button/label/input').click()
time.sleep(4)

web.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div[2]/div[7]/div/div[1]/div/span').click() # selecting professional certificate and specliazation
web.find_element_by_xpath('//*[@id="react-select-8--option-2"]/div/button/label/input').click()
time.sleep(4)

web.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div[2]/div[7]/div/div[1]/div/span').click()
web.find_element_by_xpath('//*[@id="react-select-8--option-3"]/div/button/label/input').click()
time.sleep(4)





URL = []
NAME = []
no_courses = []
xpath = []
npath = []





i = 1
n = 0
while i in range(11):
    path = '//*[@id="main"]/div/div/div[1]/div/div/div/div/div/div/ul/li[' + str(i) + ']/div'
    xpath.append(path)
    n_path = '//*[@id="main"]/div/div/div[1]/div[2]/div/div/div/div/div/ul/li[' + str(i) + ']/div/div/div/div/div/div[2]/div[1]/h2'
    npath.append(n_path)
    i += 1




while n in range(10):
    NAME.append(web.find_element_by_xpath(npath[n]).text) ## Name of professional certificate/specialization
    web.find_element_by_xpath(xpath[n]).click()
    time.sleep(4)
    web.switch_to.window(web.window_handles[1])
    URL.append(web.current_url)               ## The link for course
    try:
        web.find_element_by_xpath('//*[@id="main"]/div/div[6]/div/div/div[2]/ul/li/div[2]/button').click() # the SHOW MORE button
    except:
        pass
    try:
        b = web.find_element_by_css_selector('#main > div > div:nth-child(6) > div').text # using regex to find the number of courses by using Findall in the description of course.
        no_courses.append(len(re.findall('COURSE\n[0-9]', b)))  # adding the number of courses to courses dataset
    except:
        no_courses.append('N/A')
    web.close()
    web.switch_to.window(web.window_handles[0])
    n += 1
    if n == 10:
        web.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div/div/div/div/div/div/div[1]/div/button[7]').click()   # after iterating through 10 courses the code will move onto the next page
        n = 0
        time.sleep(4)

    print(NAME)
    print(no_courses)
    print(URL)
    print('NUMBER OF COURSES CHECKED', n)



len(NAME)          ## making sure the lengths of the lists are same
len(no_courses)
len(URL)

df = pd.DataFrame({"NAME": NAME, "URL": URL, "NUMBER OF COURSES": no_courses}) # creating a dataset using pandas
df.to_csv("coursera.csv")
df


df.to_csv("coursera.csv") # saving as csv file
backupdf = df   # back up
df.to_csv("backupcoursera.csv")  # back up csv
wk = df # working dataframe
wk = wk.replace(['N/A'],0)  # replacing N/A with 0
wk.sort_values(by=['NUMBER OF COURSES'], inplace=True) # sorting the values
wk.to_csv("sortedcoursera.csv")

print('end of code')
