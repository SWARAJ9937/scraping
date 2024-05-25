from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time


browser= webdriver.Chrome()

url= "https://healthnet.entrykeyid.com/as/authorization.oauth2?response_type=code&client_id=44eb17c3-cf1e-4479-a811-61d23ae8ffbd&scope=openid%20profile&state=zxiTit3wMFOx1RX1b859_FnniEny-q3tiHJAJHpUsRw%3D&redirect_uri=https://provider.healthnetcalifornia.com/careconnect/login/oauth2/code/pingcloud&code_challenge_method=S256&nonce=8E716IQw6mmVPlPBf2YcuFUMdAqw2EcAgXmsdPNRnJE&code_challenge=Y-9vUvIsJkcTuiCax8wTATRdffrAujd7PpEFtVG8zSM&app_origin=https://provider.healthnetcalifornia.com/careconnect/login/oauth2/code/pingcloud&brand=healthnet"
browser.get(url)
time.sleep(5)

#the below part is used to automate the log in page
mail= "rsb.ummer@sdilabsinc.com"
text_field_element= browser.find_element(By.ID,"identifierInput")
text_field_element.send_keys(mail)
login_id_element= browser.find_element(By.CLASS_NAME,"ping-button").click()#browser change
time.sleep(3)

#Below part is used to automate the password page
pwd= "Global@123"
pwd_field_element= browser.find_element(By.ID,"password")
pwd_field_element.send_keys(pwd)
login_id_element= browser.find_element(By.CLASS_NAME,"ping-button").click()#browser change

time.sleep(3)
#Landed on the Home Page
plan_type_element= browser.find_element(By.ID, "providerProfileName")
drop=Select(plan_type_element)
drop.select_by_visible_text("Commercial")
go_field_element= browser.find_element(By.ID,"medicalDropdownSubmitID").click()
time.sleep(2)
click_eligibilty=browser.find_element(By.CLASS_NAME,"eligibility").click() #browser change

time.sleep(5)
member_id="r08015821"
dob="03/14/1977"
order_date="07/15/2020"
date_of_service_element=browser.find_element(By.ID,"dos")
date_of_service_element.clear()
date_of_service_element.send_keys(order_date)
memberid_field_element= browser.find_element(By.CLASS_NAME,"input-medium")
memberid_field_element.send_keys(member_id)
birthdate_field_element= browser.find_element(By.ID,"dob")
birthdate_field_element.send_keys(dob)
eligibility_element=browser.find_element(By.NAME,"check").click()#gives the result

time.sleep(20)