from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("https://provider.caloptima.org/#/login")



# def getTableDataelegibility(typ, value)
#     table2=browser.find_element(type, value)
#     header_cells2=table.find_element(BY)

def getTableData(type, value):
    table = browser.find_element(type, value)
    header_cells = table.find_elements(By.TAG_NAME, 'th')
    headers = [cell.text.upper() for cell in header_cells]
    cells_elements = table.find_elements(By.TAG_NAME, 'td')
    cells = [data.text for data in cells_elements]

    print(headers)
    print(cells)


# Automating Login Page

# After entering the email and clicking the login button, a brief pause is introduced for synchronization.

mail = 'asfan.s@rsbhealthcareconsulting.com'
email_input_element = browser.find_element(By.ID, 'userName')
email_input_element.send_keys(mail)

#find the passward and filed and enter your passward

pwd = 'Rsb@123'
passward_field = browser.find_element(By.ID, 'txtPassword')
passward_field.send_keys(pwd)
login_id_element = browser.find_element(By.CLASS_NAME, 'controlspacer')

##Optionally, you can click the "Remember this device" checkbox
remember_device_checkbox = browser.find_element(By.CSS_SELECTOR, "span.custom-control-description")
remember_device_checkbox.click()

#Find and click the login button
login_button = browser.find_element(By.ID, "btnLogin")
login_button.click()

#Find and Verify Your Identity
# answer_security_questions = Finds(by = By.XPATH, value = 'html/body/app-providerportal/div/div/app-login/div/verify-identity/form/div[4]/div[4]/div[1]')
sucurity_element = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '/html/body/app-providerportal/div/div/app-login/div/verify-identity/form/div[4]/div[4]/div[1]'))
)
sucurity_element.click()

honeyMoonKey = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH,
                                '/html/body/app-providerportal/div/div/app-login/div/verify-identity/form/div[4]/div[4]/div[2]/div[1]/div[2]/input'))
)
honeyMoonKey.send_keys("Mysore")

childPalceKey = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH,
                                '/html/body/app-providerportal/div/div/app-login/div/verify-identity/form/div[4]/div[4]/div[2]/div[2]/div[2]/input'))
)
childPalceKey.send_keys("Bangalore")

continue_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '/html/body/app-providerportal/div/div/app-login/div/verify-identity/form/div[5]/button'))
)
continue_button.click()

claims = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '/html/body/app-providerportal/div/div[2]/app-navigator/div/div/div/div[3]/div[1]/img'))
)
claims.click()

claims_lookup = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH,
                                '/html/body/app-providerportal/div/div[3]/app-portal/div/div/app-claims-dashboard/div/div[1]/app-claims-navigation/div/div/a[1]/h4'))
)
claims_lookup.click()







elegibility_tab = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH,
                                '/html/body/app-providerportal/div/div[2]/app-navigator/div/div/div/div[2]/div[1]/img'))
)
elegibility_tab.click()





CIN_number = browser.find_element(By.ID, 'txtbxClaimCin')
CIN_number.send_keys("96942801g")
# time.sleep(200)


Find_claims = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH,
                                '/html/body/app-providerportal/div/div[3]/app-portal/div/div/app-claims-home/app-claim-lookup/div/div/div[3]/app-lookup-date/form/div[14]/button'))
)
Find_claims.click()

getTableData(By.CLASS_NAME, 'claim-table')

getTableData(By.CLASS_NAME, 'claim-table')

time.sleep(200)
