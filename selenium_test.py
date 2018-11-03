from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os

def test_home():
    option = Options()
    option.add_argument("--no-sandbox")
    option.add_argument("headless")
    driverPath = os.getcwd() + '/chromedriver'
    driver = webdriver.Chrome(driverPath, options=option)
    driver.get("http://204.209.76.213:8000/")
    
    assert driver.find_element_by_id("name") != None
    
    assert driver.find_element_by_id("about") != None
    
    assert driver.find_element_by_id("education") != None
    
    assert driver.find_element_by_id("skills") != None
    
    assert driver.find_element_by_id("work") != None
    
    assert driver.find_element_by_id("contact") != None
    
    '''

    assert driver.find_element_by_id("name") == "Sajjad Haider"
    
    assert driver.find_element_by_id("about") == "Aspiring Software Developer"
    
    assert driver.find_element_by_id("education") == "Bachelor of Science in Computing Science and Psychology"
    
    assert driver.find_element_by_id("skills") == "React,Redux,Java,Python,C"
    
    assert driver.find_element_by_id("work") == "Tangent Collective 6 months"
    
    assert driver.find_element_by_id("contact") == "780-920-8128"  
    '''
    
    
    driver.quit()

test_home()

