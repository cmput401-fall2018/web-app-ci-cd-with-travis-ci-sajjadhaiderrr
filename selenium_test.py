from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

def test_home():
    driver = webdriver.Chrome()
    driver.get("http://204.209.76.213:8000/")

    assert driver.find_element_by_id("name") == "Sajjad Haider"
    
    assert driver.find_element_by_id("about") == "Aspiring Software Developer"
    
    assert driver.find_element_by_id("education") == "Bachelor of Science in Computing Science and Psychology"
    
    assert driver.find_element_by_id("skills") == "React,Redux,Java,Python,C"
    
    assert driver.find_element_by_id("work") == "Tangent Collective 6 months"
    
    assert driver.find_element_by_id("contact") == "780-920-8128"  
    
    driver.quit()

test_home()

