from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="/Users/davidbl94/Desktop/chromedriver")

driver.get("https://productive.io/")

WebElement = WebDriverWait(driver, 5).until(
    expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div[1]/button")))

WebElement.click()
