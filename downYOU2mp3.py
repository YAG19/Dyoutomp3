from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(
    executable_path="C:\\Users\\yagne\\Downloads\\chromedriver.exe"
)
driver.minimize_window()
driver.get("https://ytmp3.cc/")

elem = driver.find_element_by_name("video")
elem.clear()


elem.send_keys(Keys.CONTROL+"v")
elem.send_keys(Keys.RETURN)

time.sleep(20)


assert "No result" not in driver.page_source
try:
    elem = driver.find_element_by_link_text("Download")
    elem.send_keys(Keys.RETURN)


    time.sleep(45)

    driver.quit()
except:
    driver.quit()
