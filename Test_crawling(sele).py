import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

URL = 'https://www.etlandmall.co.kr/pc/product/product.do?prdMstCd=S2301708'

driver = webdriver.Chrome(executable_path='chromedriver')
driver.get(url=URL)

# 현재 URL얻기 코드
# print(driver.current_url)

# 구매버튼 클릭
# driver.find_element_by_class_name('btn buy ').click()

#텍스트로 접근
# driver.find_element_by_link_text('구매하기')

#링크가 달려있는 엘레먼트에 텍스트 일부만 적어서 해당 버튼 실행('구매버튼')
btn_buy = driver.find_element_by_partial_link_text('구매')
btn_buy.click()

login_btn = driver.find_element_by_xpath('//*[@id="memberForm"]/div/ul/li[3]/a[1]')
login_btn.click()

kakao_text1 = driver.find_element_by_id('id_email_2').send_keys('이메일')
kakao_pwdd1 = driver.find_element_by_id('id_password_3').send_keys('비번')
kakao_log = driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[8]/button[1]')
kakao_log.click()

## 로그인 성공시 구매 진행
driver.implicitly_wait(10) #암묵적 5초 대기

btn_buy = driver.find_element_by_partial_link_text('구매')
btn_buy.click() # 구매버튼 클릭

LavelCode = driver.find_element_by_xpath('//*[@id="LGD_PAYINFO"]/div[5]/div[1]/div[3]/div/ul/li[6]/div/div/div/ol/li[6]/a')
LavelCode.click()

element = driver.find_element_by_class_name('a_list')
driver.execute_script('arguments[5].click();',element)


None_credit = driver.find_element_by_xpath('//*[@id="LGD_PAYINFO"]/div[5]/div[1]/div[6]/a[11]')
None_credit.click() #무통장 클릭

# 브라우저 닫기 코드
# driver.close()