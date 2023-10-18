from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()  # Chrome 드라이버를 사용

# 일루미나리안 사이트로 이동
driver.get("https://illuminarean.com/")

try:
    # [Work] 메뉴 클릭
    element = driver.find_element(By.CSS_SELECTOR, "#__next > div > header > div > div > div > div > nav > ul > li:nth-child(2) > a > span")
    element.click()
    
    # [GOODVIBE WORKS 바로가기] 메뉴 클릭
    element = driver.find_element(By.CSS_SELECTOR,("#__next > div > main > div > div:nth-child(2) > div > div.css-s49xw9.edcyzk41 > div > a")
    element.click()
    
    # [무료체험신청] 메뉴 클릭
    free_trial_menu = driver.find_element_by_link_text("무료체험신청")
    free_trial_menu.click()
    
    # 내용 입력
    content_input = driver.find_element_by_id("content")
    content_input.send_keys("내용을 입력하세요.")
    
    # 담당 업무 리스트에서 클릭으로 1개 선택
    # 예를 들어, 첫 번째 업무를 클릭으로 선택
    task_list = driver.find_elements_by_css_selector(".task-list .task")
    if len(task_list) > 0:
        task_list[0].click()
    
    # 담당 업무 리스트에서 검색으로 1개 선택
    # 예를 들어, 검색어를 입력하고 검색 버튼을 클릭
    search_input = driver.find_element_by_id("searchInput")
    search_input.send_keys("검색어를 입력하세요.")
    search_button = driver.find_element_by_id("searchButton")
    search_button.click()
    
    # 신청 취소
    # 이 부분에서 무료 이용 신청 버튼을 클릭하지 않도록 설정
    
    # 몇 초 동안 대기
    sleep(5)
    
finally:
    # 브라우저 종료
    driver.quit()
