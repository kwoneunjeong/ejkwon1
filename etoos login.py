from selenium import webdriver
from selenium.webdriver.common.by import By

# 웹 드라이버 초기화
driver = webdriver.Chrome()  # Chrome 드라이버를 사용
u = 'https://member.etoos.com/login?clientId=127ed5791eb71160f674421ad5da30f67672e7c9&callbackUrl=https%3A%2F%2Fwww.etoos.com%2Fmember%2Finte_mem%2Finte_login.asp&joinCallbackUrl=https%3A%2F%2Fwww.etoos.com%2Fmember%2Finte_mem%2Finte_join.asp&returnURL=https%3A%2F%2Fwww.etoos.com%2Fhome%2Fdefault.asp%3F'
driver.get(u)

#사용자 이름과 비밀번호 입력 후 로그인 버튼 클릭 
username = "dmswjddl83"
password = "zz112233!"

for i in range(1,10):
    print("pass")

driver.execute_script ("document.querySelectorAll('input[type=text]')[0].value='dmswjddl83'")
driver.execute_script ("document.querySelectorAll('input[type=password]')[0].value='zz112233!'")


#  로그인 버튼 클릭
driver.find_element(By.XPATH,'//*[@id="contents"]/div/div/button').click()







