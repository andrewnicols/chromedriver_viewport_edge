import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1366,708")
options.add_argument("--disable-dev-shm-usage")
options.headless = False
driver = webdriver.Remote(
    command_executor="http://127.0.0.1:4444/wd/hub",
    options=options,
)

driver.get("http://host.docker.internal:8880/index.html")
elem = driver.find_element(By.LINK_TEXT, "Course participation")
elem.click()
driver.save_screenshot('screenshot.png')
assert "Course administration" not in driver.page_source
driver.close()
