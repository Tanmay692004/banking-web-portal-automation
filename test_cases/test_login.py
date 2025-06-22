from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_banking_login():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get("https://demo.guru99.com/V4/")

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.NAME, "uid"))).send_keys("mngr511728")
    driver.find_element(By.NAME, "password").send_keys("YgAdAvU")
    driver.find_element(By.NAME, "btnLogin").click()

    assert "Manager" in driver.page_source
    driver.quit()
