from selenium import webdriver

driver = webdriver.Chrome('/Users/jeongbyeongju/Downloads/chromedriver')
driver.implicitly_wait(2)
driver.get('https://www.daum.net/')