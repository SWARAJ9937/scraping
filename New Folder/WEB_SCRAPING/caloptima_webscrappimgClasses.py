from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("https://provider.caloptima.org/#/login")


def getTableData(type, value, sleepTime):
    time.sleep(sleepTime)
    table = browser.find_element(type, value)
    header_cells = table.find_elements(By.TAG_NAME, 'th')
    headers = [cell.text.upper() for cell in header_cells]
    cells_elements = table.find_elements(By.TAG_NAME, 'td')
    cells = [data.text for data in cells_elements]

    print(headers)
    print(cells)


def clickByClassName(className):
    button = browser.find_element(By.CLASS_NAME, className)
    button.click()


def clickByCssSelector(cssSelector):
    button = browser.find_element(By.CSS_SELECTOR, cssSelector)
    button.click()


def clickById(id):
    button = browser.find_element(By.ID, id)
    button.click()

def clickByWebDriverWait(value, timeOut):
    button = WebDriverWait(browser, timeOut).until(EC.element_to_be_clickable((By.XPATH, value)))
    button.click()

def sendValueInWebDriverWait(key, timeOut, value):
    input = WebDriverWait(browser, timeOut).until(
        EC.element_to_be_clickable((By.XPATH, key))
    )
    input.send_keys(value)

def clickByIdAndSendValue(id , value):
    button = browser.find_element(By.ID, id)
    button.send_keys(value)

def getXPathValues(xpath):
    value = browser.find_element(By.XPATH, xpath)
    return value.text

def getClassValues(className):
    value = browser.find_element(By.CLASS_NAME, className)
    return value.text

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
clickByCssSelector("span.custom-control-description")

#Find and click the login button
clickById("btnLogin")

#Find and Verify Your Identity
# answer_security_questions = Finds(by = By.XPATH, value = 'html/body/app-providerportal/div/div/app-login/div/verify-identity/form/div[4]/div[4]/div[1]')
clickByWebDriverWait('/html/body/app-providerportal/div/div/app-login/div/verify-identity/form/div[4]/div[4]/div[1]', 20)

#security question 1
sendValueInWebDriverWait('/html/body/app-providerportal/div/div/app-login/div/verify-identity/form/div[4]/div[4]/div[2]/div[1]/div[2]/input', 10, "Mysore")

#security question 2
sendValueInWebDriverWait('/html/body/app-providerportal/div/div/app-login/div/verify-identity/form/div[4]/div[4]/div[2]/div[2]/div[2]/input', 10, "Bangalore")

# click on login button
clickByWebDriverWait('/html/body/app-providerportal/div/div/app-login/div/verify-identity/form/div[5]/button', 15)

#Eleglibity
clickByWebDriverWait('/html/body/app-providerportal/div/div[2]/app-navigator/div/div/div/div[2]/div[1]', 15)
time.sleep(5)
#MemberId
clickByIdAndSendValue('memberIdInput', '96942801g')

#Submit Button for MemberId
clickByWebDriverWait('/html/body/app-providerportal/div/div[3]/app-portal/div/div/app-member/div/div/div[2]/app-member-search/div/div/p-tabview/div/div/p-tabpanel[1]/div/div/form/div[2]/button', 10)

#GetValues
time.sleep(5)
values = getClassValues("member-result-container-grid")
split_list = values.split('\n')
print(values)
time.sleep(10)


print(" ===============================\n")


print('claims')
# click on claim status button
clickByWebDriverWait('/html/body/app-providerportal/div/div[2]/app-navigator/div/div/div/div[3]/div[1]/img', 15)


#click on claims lookup
clickByWebDriverWait('/html/body/app-providerportal/div/div[3]/app-portal/div/div/app-claims-dashboard/div/div[1]/app-claims-navigation/div/div/a[1]/h4', 15)


#click on the cin number
CIN_number = browser.find_element(By.ID, 'txtbxClaimCin')

#give the value of cin number
CIN_number.send_keys("96942801g")
# time.sleep(200)

#click on find claims
clickByWebDriverWait('/html/body/app-providerportal/div/div[3]/app-portal/div/div/app-claims-home/app-claim-lookup/div/div/div[3]/app-lookup-date/form/div[14]/button', 15)

#get table data on class name or we can say it reading the data
getTableData(By.CLASS_NAME, 'claim-table', 10)



time.sleep(5)
browser.quit()