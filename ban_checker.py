from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

DRIVER_PATH = './drivers/chromedriver/chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
service = Service(executable_path=DRIVER_PATH)

def check_user(username):
    try:
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(f'https://www.twitch.tv/popout/{username}/chat?popout=')
        ban_status = "suspended" in driver.find_element(By.CLASS_NAME, 'chat-line__status').text

        if (ban_status):
            print(f'\n{username} has been banned!\n')
            return True
        else:
            #print(f'\n{username} is not yet banned.\n')
            return False
        
    except NoSuchElementException: 
            #print(f'\n{username} is not yet banned.\n')
            return False
        
    finally:
        driver.quit()
        