from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import json,time
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException,JavascriptException

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
    except (NoSuchElementException, TimeoutException) as error:
        return json.dumps({
            "Result": None,
            "Status": "Failure",
            "Error": error.__class__.__name__,
            "Location of Error":"Error at Login Page",
            "Explanation": str(error)
            },indent=4)
    return json.dumps({"Success": True})
 
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
    except (NoSuchElementException, TimeoutException)as error:
        return json.dumps({
            "Result": None,
            "Status": "Failure",
            "Error": error.__class__.__name__,
            "Location of Error":f"Error at Navigating Plan Type for {plan_type}",
            "Explanation": str(error)
            },indent=4)
    return json.dumps({"success": True})
 
def handle_exception(broswer, birth_date,member_id,order_date):
    while True:
        try:
            
            #the below is for orderdate input
            js_script = """
            var el = document.getElementById('dos');
            el.value = arguments[0];
            el.dispatchEvent(new Event('input'));
            el.dispatchEvent(new Event('change'));
            """
            broswer.execute_script(js_script, order_date)
            time.sleep(2)

            #the below is for birthdate input
            js_script = """
            var el = document.getElementById('dob');
            el.value = arguments[0];
            el.dispatchEvent(new Event('input'));
            el.dispatchEvent(new Event('change'));
            """
            broswer.execute_script(js_script, birth_date)
            time.sleep(2)

            #the below is for mem_id input
            js_script = """
            var el = document.getElementById('memberIdOrLastName');
            el.value = arguments[0];
            el.dispatchEvent(new Event('input'));
            el.dispatchEvent(new Event('change'));
            """
            broswer.execute_script(js_script, member_id)


            # time.sleep(2)
            # date_of_service_element = broswer.find_element(By.NAME,"dos")
            # date_of_service_element.clear()
            # print(order_date)
            # broswer.execute_script("arguments[0].setAttribute('name', arguments[1]);", date_of_service_element, order_date)

            # time.sleep(2)
            # memid_element= broswer.find_element(By.CLASS_NAME, "input-medium")
            # memid_element.clear()
            # print(member_id)
            # memid_element.send_keys(member_id)

            # time.sleep(2)
            # dob_element= WebDriverWait(broswer,10).until(EC.presence_of_element_located((By.ID,"dob")))
            # dob_element.clear()
            # print(birth_date)
            # dob_element.send_keys(birth_date)

            broswer.find_element(By.NAME, "check").click()
            WebDriverWait(broswer, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "icon-status")))
            break
 
        except (NoSuchElementException,UnexpectedAlertPresentException,TimeoutException,JavascriptException)as error:
            actions = ActionChains(broswer)
            actions.send_keys(Keys.ENTER).perform()
            time.sleep(1)
            # return json.dumps({
            # "Result": None,
            # "Status": "Failure",
            # "Error": error.__class__.__name__,
            # "Location of Error":f"Error at Handling Exception",
            # "Explanation": str(error)
            # },indent=4)
            continue
        
def eligibility_check(browser, id, birth_date, order_date, plan_types):
    eligibilty_results = {
        "Member ID": id,
        "DOB": birth_date
        }
    checker=eligibilty_results.copy()
 
   
    for plan_type in plan_types:
        print(f"Eligibilty Check For Plan Type: {plan_type}")
        browser.switch_to.default_content()
        response = navigate_to_plan_type(browser, plan_type)

        if json.loads(response).get("error"):
            eligibilty_results[plan_type] = response
            continue
       
        browser.find_element(By.CLASS_NAME, "eligibility").click()
        handle_exception(browser,birth_date,id,order_date) #for eligibility only.


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
 
        except (NoSuchElementException, TimeoutException) as error:
            return json.dumps({
            "Result": None,
            "Status": "Failure",
            "Error": error.__class__.__name__,
            "Location of Error":f"Error at Eligibilty Check for {plan_type}",
            "Explanation": str(error)
            },indent=4)
        

    if checker==eligibilty_results:
        return json.dumps({
            "Result": "Eligibity of the Person not Found",
            "Status": "Success"
            },indent=4)
    else:
        return json.dumps({
            "Result":eligibilty_results,
            "Status": "Success"
            },indent=4)
       
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

        while True:  #this below part will retry to give the input if an error is in date is coming.
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

                if error in "The Member ID number specified does not match any in our records":
                    break

                match_error = "From Date is required. To Date is required. Please enter the date in a valid format (MM/DD/YYYY)."
 
                if error in match_error:
                    print("Matching error detected, retrying input submission...")
                    continue

                break #this line will not be reached until and unless the above condition is false.

            except NoSuchElementException:
                print("Proceeding with the claim check...")
                break  

        #the below part is used to scrape the claim results.   
        try:
            time.sleep(2)
            table = browser.find_element(By.CLASS_NAME, 'table')
            header_cells = table.find_elements(By.TAG_NAME, 'th')
            headers = [cell.text.upper() for cell in header_cells]
            cells_elements = table.find_elements(By.TAG_NAME, 'td')
            cells = [data.text for data in cells_elements]
 
            claim_data = dict(zip(headers, cells))
            claim_results[plan_type] = claim_data

 
        except NoSuchElementException as error:
            continue

        except TimeoutException as error:
            return  json.dumps({
                "Result": "Found an error.",
                "Status":"Failed",
                "Error": error
            })
        
    if claim_results==checker:
        return json.dumps({
            "Result": "Claim Check for the given details couldnt be found",
            "Status": "Success",
            },indent=4)
    else:
        return json.dumps({
            "Result": claim_results,
            "Status": "Success",
            },indent=4)
    
def main():
    try:
        mail = "rsb.ummer@sdilabsinc.com"
        pwd = "Global@123"
        url= "https://sso.entrykeyid.com/as/authorization.oauth2?response_type=code&client_id=44eb17c3-cf1e-4479-a811-61d23ae8ffbd&scope=openid%20profile&state=EDw09ZAb3E_OsHIKpp5aXISg94vgcB3svG5lY7BCIWE%3D&redirect_uri=https://provider.healthnetcalifornia.com/careconnect/login/oauth2/code/pingcloud&code_challenge_method=S256&nonce=Vxy-bb518dRU7mRJuhn_Puem4jy6rytiVU1litsor60&code_challenge=V1DUWjTGEiVH1WFBK8d_FxAXTMpuZ6ztwqrSUOFEifU&app_origin=https://provider.healthnetcalifornia.com/careconnect/login/oauth2/code/pingcloud&brand=healthnet"
        browser = initialize_browser(url)
        login_response = login_to_portal(browser, mail, pwd)
        if json.loads(login_response).get("error"):
            print(login_response)
            return
    
        # id_input = input("Enter the member id: ")
        # dob_input = input("Enter the dob of patient in mm/dd/yyy format: ")
        # dos_input = input("Enter the date of service in mm/dd/yyy format: ")

        plan_types=["Commercial","MediCal","Medicare"]  
        
        id_input="99256925G"
        dob_input="07/26/2019"
        dos_input="01/18/2024"

        eligibility_result = eligibility_check(browser, id_input, dob_input, dos_input, plan_types)
        print(eligibility_result)
    
        claim_result = claim_check(browser, id_input, dob_input, dos_input, plan_types)
        print(claim_result)

        print("\n\n###########################\n\n")

        id_input="R0755496400"
        dob_input="12/12/1973"
        dos_input="01/19/2024"

        eligibility_result = eligibility_check(browser, id_input, dob_input, dos_input, plan_types)
        print(eligibility_result)
    
        claim_result = claim_check(browser, id_input, dob_input, dos_input, plan_types)
        print(claim_result)

        print("\n\n###########################\n\n")

        id_input="R07780209FM1"
        dob_input="04/04/2024"
        dos_input="01/20/2024"

        eligibility_result = eligibility_check(browser, id_input, dob_input, dos_input, plan_types)
        print(eligibility_result)
    
        claim_result = claim_check(browser, id_input, dob_input, dos_input, plan_types)
        print(claim_result)


        print("\n\n###########################\n\n")

        id_input="U9318486101"
        dob_input="11/23/1967"
        dos_input="12/08/2022"

        eligibility_result = eligibility_check(browser, id_input, dob_input, dos_input, plan_types)
        print(eligibility_result)
    
        claim_result = claim_check(browser, id_input, dob_input, dos_input, plan_types)
        print(claim_result)

        print("\n\n###########################\n\n")

        id_input="R1154921432"
        dob_input="12/16/1962"
        dos_input="10/24/2022"

        eligibility_result = eligibility_check(browser, id_input, dob_input, dos_input, plan_types)
        print(eligibility_result)
    
        claim_result = claim_check(browser, id_input, dob_input, dos_input, plan_types)
        print(claim_result)

        print("\n\n###########################\n\n")

        id_input="U9364746003"
        dob_input="05/12/2000"
        dos_input="10/24/2022"    
    
        eligibility_result = eligibility_check(browser, id_input, dob_input, dos_input, plan_types)
        print(eligibility_result)
    
        claim_result = claim_check(browser, id_input, dob_input, dos_input, plan_types)
        print(claim_result)

    except TimeoutException as error:
        return json.dumps({
                "Result": None,
                "Status": "Failure",
                "Error": error.__class__.__name__,
                "Explanation": str(error)
                },indent=4)
        
if __name__ == "__main__":
    main()