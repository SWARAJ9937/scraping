from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import json
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
import time

def initialize_browser(url):
    browser = webdriver.Chrome()
    browser.get(url)
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    return browser

def login_to_portal(browser, mail, pwd):
    try:
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "username"))).send_keys(mail)
        browser.find_element(By.CLASS_NAME, "MuiButtonBase-root").click()
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "password"))).send_keys(pwd)
        browser.find_element(By.CLASS_NAME, "MuiButtonBase-root").click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    except (NoSuchElementException, TimeoutException) as e:
        return json.dumps({"error": "Error logging in. Please check the login steps."})
    return json.dumps({"success": True})

def navigate_to_plan_type(browser, plan_type):
    plan_types = {
        "Commercial": "Commercial",
        "MediCal": "Medi-Cal",
        "Medicare": "Medicare/DSNP Integrated Plans"
    }
    if plan_type not in plan_types:
        return json.dumps({"error": "Invalid plan type."})

    try:
        plan_type_element = Select(WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "providerProfileName"))))
        plan_type_element.select_by_visible_text(plan_types[plan_type])
        time.sleep(2)
        actions = ActionChains(browser)
        actions.send_keys(Keys.ESCAPE).perform()
        time.sleep(1)
        browser.find_element(By.ID, "medicalDropdownSubmitID").click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    except (NoSuchElementException, TimeoutException):
        return json.dumps({"error": "Failed to navigate to specified plan type."})
    return json.dumps({"success": True})

def handle_exception(broswer, input_details):
    birth_date= input_details["d_o_b"]
    member_id= input_details["m_id"]
    order_date= input_details["d_o_s"]
    
    while True:
        try:
            dob_element= WebDriverWait(broswer,10).until(EC.presence_of_element_located((By.ID,"dob")))
            dob_element.clear()
            dob_element.send_keys(birth_date)

            date_of_service_element = WebDriverWait(broswer,10).until(EC.presence_of_element_located((By.ID, "dos")))
            date_of_service_element.clear()
            date_of_service_element.send_keys(order_date)

            name_element= broswer.find_element(By.CLASS_NAME, "input-medium")
            name_element.clear()
            name_element.send_keys(member_id)
            break

        except UnexpectedAlertPresentException:
            continue
        
    broswer.find_element(By.NAME, "check").click()
    WebDriverWait(broswer, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "icon-status"))) 

def eligibility_check(browser, id, birth_date, order_date, plan_types):
    eligibilty_results = {
        "Member ID": id,
        "DOB": birth_date
        }
    checker=eligibilty_results.copy()

    input_details={
        "d_o_b": birth_date,
        "m_id": id,
        "d_o_s": order_date
    }
    
    for plan_type in plan_types:
        print(f"Eligibilty Check For Plan Type: {plan_type}")
        browser.switch_to.default_content()
        response = navigate_to_plan_type(browser, plan_type)
        if json.loads(response).get("error"):
            eligibilty_results[plan_type] = response
            continue
        
        browser.find_element(By.CLASS_NAME, "eligibility").click()
        handle_exception(browser,input_details)

        try:
            table = browser.find_element(By.CLASS_NAME, 'table')
            header_cells = table.find_elements(By.TAG_NAME, 'th')
            headers = [cell.text.upper() for cell in header_cells]
            cells_elements = table.find_elements(By.TAG_NAME, 'td')
            cells = [data.text for data in cells_elements]

            store_data = True

            if plan_type=="Commercial":

                indices_to_keep = [0, 1, 2, 4, 5]
                headers = [headers[i] for i in indices_to_keep]

                cells[0] = table.find_element(By.CLASS_NAME, "icon-status").get_attribute("title")
                cells[2] = cells[2].split("\n")[0]
                cells[5] = cells[5].split("\n")
                cells[6] = " ".join(cells[5])
                cells = [cells[i] for i in indices_to_keep]
                data_dict = dict(zip(headers, cells))
            elif plan_type=="Medicare":

                indices_to_keep = [0, 1, 2, 4]
                headers = [headers[i] for i in indices_to_keep]
                cells[0]= table.find_element(By.CLASS_NAME,"icon-status").get_attribute("title")
                cells[2]= cells[2].split("\n")[0]
                cells = [cells[i] for i in indices_to_keep]
                
                data_dict= dict(zip(headers,cells))
            else:

                indices_to_keep = [0, 1, 2, 4, 6]
                headers = [headers[i] for i in indices_to_keep]
                cells[0] = table.find_element(By.CLASS_NAME, "icon-status").get_attribute("title")
                cells[2] = cells[2].split("\n")[0]
                cells[6] = cells[6].split("\n")
                cells[6] = " ".join(cells[6])
                cells = [cells[i] for i in indices_to_keep]
                
                data_dict = dict(zip(headers, cells))
            
            if 'PATIENT NAME' in data_dict:
                patient_name = data_dict['PATIENT NAME'].strip().lower()
                if patient_name == 'no members found.' or \
                patient_name == f"medicare/dsnp integrated plans patient not found. ({id} & {birth_date})".lower() or \
                patient_name == f"Commercial Patient not found. ({id} & {birth_date})".lower() or \
                patient_name== f"date of service is not a valid date.":
                    store_data = False

            if store_data:
                eligibilty_results[plan_type] = data_dict
            else:
                eligibilty_results.pop(plan_type, None)

        except (NoSuchElementException, TimeoutException) as e:
            pass

    if checker==eligibilty_results:
        return "Eligibilty Of The Given details Not Found"
    else:
        return json.dumps(eligibilty_results,indent=4)
        
def claim_check(browser, id, birth_date, order_date, plan_types):

    claim_results = {
        "Member ID": id,
        "DOB": birth_date
    }

    checker=claim_results.copy()

    for plan_type in plan_types:
        print(f"Claim Check For Plan Type: {plan_type}")
        browser.switch_to.default_content()
        response = navigate_to_plan_type(browser, plan_type)
        
        if json.loads(response).get("error"):
            claim_results[plan_type] = response
            continue
        while True:
            try:
                browser.find_element(By.CLASS_NAME, "claims").click()
                WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "icon-action-search"))).click()
                id_element = browser.find_element(By.CLASS_NAME, "input-medium")
                id_element.clear()
                id_element.send_keys(id)
                
                from_date = browser.find_element(By.ID, "dosFrom")
                from_date.clear()
                from_date.send_keys(order_date)

                to_date = browser.find_element(By.ID, "dosTo")
                to_date.clear()
                to_date.send_keys(order_date)

                actions = ActionChains(browser)
                actions.send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()

                error_element = browser.find_element(By.ID, "claimStatusModel.errors")
                error = error_element.text
                match_error = "From Date is required. To Date is required."

                if error == match_error:
                    print("Matching error detected, retrying input submission...")
                    continue  
          
                break

            except NoSuchElementException:
                break  
            
        try:
            WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "mem-cellwidth")))
            table = browser.find_element(By.CLASS_NAME, 'table')
            header_cells = table.find_elements(By.TAG_NAME, 'th')
            headers = [cell.text.upper() for cell in header_cells]
            cells_elements = table.find_elements(By.TAG_NAME, 'td')
            cells = [data.text for data in cells_elements]

            claim_data = dict(zip(headers, cells))
            claim_results[plan_type] = claim_data

        except NoSuchElementException:
            pass
        except (TimeoutException, Exception):
            pass
    if claim_results==checker:
        return "Claim Status not found for given details"
    else:
        return json.dumps(claim_results, indent=4)

def main():
    mail = "rsb.ummer@sdilabsinc.com"
    pwd = "Global@123"
    url= "https://healthnet.entrykeyid.com/as/authorization.oauth2?response_type=code&client_id=44eb17c3-cf1e-4479-a811-61d23ae8ffbd&scope=openid%20profile&state=zxiTit3wMFOx1RX1b859_FnniEny-q3tiHJAJHpUsRw%3D&redirect_uri=https://provider.healthnetcalifornia.com/careconnect/login/oauth2/code/pingcloud&code_challenge_method=S256&nonce=8E716IQw6mmVPlPBf2YcuFUMdAqw2EcAgXmsdPNRnJE&code_challenge=Y-9vUvIsJkcTuiCax8wTATRdffrAujd7PpEFtVG8zSM&app_origin=https://provider.healthnetcalifornia.com/careconnect/login/oauth2/code/pingcloud&brand=healthnet"
    browser = initialize_browser(url)
    login_response = login_to_portal(browser, mail, pwd)
    if json.loads(login_response).get("error"):
        print(login_response)
        return
    
    # id_input = input("Enter the member id: ")
    # dob_input = input("Enter the dob of patient in mm/dd/yyy format: ")
    # dos_input = input("Enter the date of service in mm/dd/yyy format: ")
    # plan_types=["Commercial","MediCal","Medicare"]    
    id_input="96971762F"
    dob_input="01/03/2012"
    dos_input="01/18/2024"
    plan_types = "Medi-cal"
    

    # id_input="97390174E"
    # dob_input="03/14/1977"
    # dos_input="01/12/2024"
    

    # id_input="99256925G"
    # dob_input="07/26/2019"
    # dos_input="01/18/2024"
    
    
    eligibility_result = eligibility_check(browser, id_input, dob_input, dos_input, plan_types)
    print(eligibility_result)

    # claim_result = claim_check(browser, id_input, dob_input, dos_input, plan_types)
    # print(claim_result)

if __name__ == "__main__":
    main()
