from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="/Users/davidbl94/Desktop/chromedriver")

driver.get("https://beta.infinum.com/the-capsized-eight")

WebElement = WebDriverWait(driver, 10).until(
    expected_conditions.presence_of_element_located((By.XPATH, "/html/body/main/div/header/nav/div/a[3]")))

WebElement.click()

business = WebDriverWait(driver, 10).until(
    expected_conditions.presence_of_element_located((By.CLASS_NAME, "__highlight")))

assert business.text == 'Business'
#driver.quit()