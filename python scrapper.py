#this scrapper scraps according to pixels because in twitter at a time only few tweets are loaded and we have to keep scrolling and scrapping at the same time
from selenium import webdriver
import pandas as pd
import time

#download chrome webdriver and provide path here***********************************************************
driver = webdriver.Chrome("C:/Users/Vivek/Downloads/chromedriver")

#address here of the website you want to scrape data from************************************************************
driver.get("https://twitter.com/indiatoday?lang=en") # i tried scrapping this twitter page

content = driver.page_source
driver.maximize_window()

SCROLL_PAUSE_TIME = 0.5
sc=30 #number of down scroll
l=[]
while sc>0:
    # Scroll down by 500 pixel
    driver.execute_script("window.scrollTo(0, window.scrollY + 500);","")
    a=200
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    sc-=1
    
    #****************************************************************************
    #change xpath according to the website's div/span/class to uniquely identify area of data(paragraph or sentences in html).
    #change it after looking at the websites's elements in developer tools
    cards = driver.find_elements_by_xpath('//div[@class="css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"]') 
    #for me this is the xpath of tweet it is different for different websites
    
    for i in range(len(cards)):
        st=str(cards[i].text).split()
        if len(st)>2:       #this condition is just to eliminate one/two word sentences.
            string='"'+str(" ".join((cards[i].text).split()))+'"'
            if string in l:
                continue
            else:
                l.append(string)

#storing in csv file
output = pd.DataFrame({"scrapped sentences":l})
output.to_csv('testdata.tsv',index=False,quoting=3, escapechar='\\')

#if you want the browser to stop at the end uncomment next line
#driver.quit()


