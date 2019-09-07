from selenium import webdriver
import time

def rollnet(url):
     a = webdriver.Edge()
     a.get(url)
     for i in range(15):
       a.execute_script('window.scrollTo(0,100000)')
       time.sleep(1.5)
     p = a.page_source  
     a.close()
     return p
    
    
