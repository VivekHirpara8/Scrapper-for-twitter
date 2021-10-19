from selenium import webdriver
import pandas as pd
import time

driver = webdriver.Chrome("C:/Users/Vivek/Downloads/chromedriver")


#address here************************************************************
driver.get("https://twitter.com/indiatoday?lang=en")
#my own html************************************************************
#driver.get("C:/Users/Vivek/Desktop/VIVEK/mini%20project/Sentiment-Analysis-using-Naive-Bayes-Classifier-master/Source/tweets_data.html")


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
    
    
    #change class accordingly to identify unique sentences*****************************************
    cards = driver.find_elements_by_xpath('//div[@class="css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"]')
    #cards= driver.find_elements_by_xpath('//dt[@class="a"]')
    #****************************************************************************    
    
    for i in range(len(cards)):
        st=str(cards[i].text).split()
        if len(st)>2:
            string='"'+str(" ".join((cards[i].text).split()))+'"'
            if string in l:
                continue
            else:
                l.append(string)
 
output = pd.DataFrame({"review":l[1:]})
output.to_csv('testdata.tsv',index=False,quoting=3, escapechar='\\')

# if you want the browser to stop at the end uncomment next line
#driver.quit()


