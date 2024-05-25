from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser= webdriver.Chrome()
url = 'https://sso.entrykeyid.com/as/authorization.oauth2?response_type=code&client_id=44eb17c3-cf1e-4479-a811-61d23ae8ffbd&scope=openid%20profile&state=6fgaGge-1S7b8eTxDq-fddgr9esmvF-iJ9YTWz8_UkY%3D&redirect_uri=https://provider.healthnetcalifornia.com/careconnect/login/oauth2/code/pingcloud&code_challenge_method=S256&nonce=D7JJSRqDYzYbvUbSfzSZTsLGs7oljBXx2L-i63D9UtU&code_challenge=wOO9vpuNmm8pPczCgfV_O8a0FGX8FBtizgCVyvru0ng&app_origin=https://provider.healthnetcalifornia.com/careconnect/login/oauth2/code/pingcloud&brand=healthnet'
browser.get(url)
time.sleep(3)


#Below part is used to automate the login page
mail = 'rsb.ummer@sdilabsinc.com'
email_text_input = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID,'username')))
email_text_input.send_keys(mail)
login_button_email = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID,"nextButton")))
login_button_email.click()
time.sleep(3)

#It is used to automate the passward page
passward = 'Global@123'
passward_input_element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID , 'password')))
passward_input_element.send_keys(passward)
passward_login_login = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID,'loginButton')))
passward_login_login.click()
time.sleep(25)

#It used to automate the go button and select the plan type
go_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/header/nav[2]/div/div[1]/form/div/div[4]/button')))
go_button.click()
eligibility_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'eligibility')))
eligibility_button.click()
time.sleep(5)

input_dos = '01/18/2024'
input_element_date = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'dos')))
input_element_date.clear()
input_element_date.send_keys(input_dos)
time.sleep(4)

memberid='99256925G'
input_element_memderid = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'memberIdOrLastName')))
input_element_memderid.send_keys(memberid)

dob='07/26/2019'
input_element_dob = WebDriverWait(browser, 12).until(EC.element_to_be_clickable((By.ID, 'dob')))
input_element_dob.send_keys(dob)


check_eligibility_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn btn-success')))
check_eligibility_button[0].click()
time.sleep(10)






