from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/')

driver.execute_script ("document.getElementById('id').value= 'dmswjddl830'")
driver.execute_script ("document.getElementById('pw').value= 'a!3342739'")

driver.find_element(By.XPATH,'//*[@id="log.login"]').click()