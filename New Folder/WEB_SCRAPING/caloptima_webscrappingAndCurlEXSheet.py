from seleniumwire import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests
import gzip
import json
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta


# Configure the Selenium Wire options to capture network traffic
seleniumwire_options = {
    'enable_har': True
}

screen_width = 1024
screen_height = 768

options = Options()
options.add_experimental_option("detach", True)
options.add_argument(f"--window-size={screen_width},{screen_height}")
service = Service(executable_path='chromium.chromedriver')

# Initialize the WebDriver with Selenium Wire
driver = webdriver.Chrome(service=service, options=options, seleniumwire_options=seleniumwire_options)

def clickByWebDriverWait(value, timeOut):
    button = WebDriverWait(driver, timeOut).until(EC.element_to_be_clickable((By.XPATH, value)))
    button.click()

def sendValueInWebDriverWait(key, timeOut, value):
    input = WebDriverWait(driver, timeOut).until(
        EC.element_to_be_clickable((By.XPATH, key)))
    input.send_keys(value)

def callCaloptima(bearer, data):
    # The URL to which the request is being sent
    url = 'https://providerservice.caloptima.org/api/member/getMembersById'

    # Headers as specified in the curl request
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
        'Access-Control-Request-Headers': 'authorization,content-type,identifier',
        'Access-Control-Request-Method': 'POST',
        'Authorization': 'Bearer '+bearer,
        'Content-Type': 'application/json',
        'identifier': '17124829179990.23228819479715557',
    }

    # Making the POST request
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Checking the response and printing accordingly
    if response.status_code == 200:
        print("Request was successful.")
        print(response.json())
        return response.json()
    else:
        print(f"Request failed with status code: {response.status_code}")
        return {}
      
def callCaloptimaGetProviderClaimsByCriteria(claims_data):  
    url = 'https://providerservice.caloptima.org/api/claim/getProviderClaimsByCriteria'

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
        'Content-Type': 'application/json',
        'Origin': 'https://provider.caloptima.org',
        'Referer': 'https://provider.caloptima.org/',
        'identifier': '17124667353440.1779999597943962',
    }

    
    response = requests.post(url, headers=headers, data=json.dumps(claims_data))
    if response.status_code == 200:
        print("Request was successful.")
        print(response.json())
        return response.json()
    else:
        print("Request failed with status code:", response.status_code)
        return {}

def get_response_bodies(driver, target_url):
    # Wait for a specific network request
    driver.wait_for_request(target_url, timeout=30)

    # List to hold the response bodies
    response_bodies = []

    # Iterate through the requests
    for request in driver.requests:
        if request.response and request.url == target_url:
            content_type = request.response.headers.get('Content-Type', '')
            content_encoding = request.response.headers.get('Content-Encoding', '')

            # Handle based on Content-Encoding
            body = None
            if 'gzip' in content_encoding:
                compressed_body = request.response.body
                if compressed_body:
                    try:
                        decompressed_body = gzip.decompress(compressed_body)
                        if 'text' in content_type or 'json' in content_type:
                            body = decompressed_body.decode('utf-8')
                        else:
                            body = decompressed_body
                    except Exception as e:
                        print(f"Error decompressing response: {e}")
            else:
                try:
                    if 'text' in content_type or 'json' in content_type:
                        body = request.response.body.decode('utf-8')
                    else:
                        body = request.response.body
                except Exception as e:
                    print(f"Error decoding response: {e}")

            if body is not None:
                response_bodies.append(json.loads(body))

    return response_bodies

try :

    output_filename = 'Cal-potimeResponse.xlsx'
    dataListResponse = []

    now = datetime.utcnow()
    timestamp = now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")[:-3] + "Z"
    one_year_back = now - relativedelta(years=1)
    one_year_back_timestamp = one_year_back.strftime("%Y-%m-%dT%H:%M:%S.%fZ")[:-3] + "Z"
    
    driver.get("https://provider.caloptima.org/#/login")

    # Your existing code to interact with the web page
    mail = 'asfan.s@rsbhealthcareconsulting.com'
    email_input_element = driver.find_element(By.ID, 'userName')
    email_input_element.send_keys(mail)

    pwd = 'Rsb@1234'
    password_field = driver.find_element(By.ID, 'txtPassword')
    password_field.send_keys(pwd)

    login_button = driver.find_element(By.ID, 'btnLogin')
    login_button.click()

    #Find and Verify Your Identity
    clickByWebDriverWait('/html/body/app-providerportal/div/div/app-login/div/verify-identity/form/div[4]/div[4]/div[1]', 20)

    #security question 1
    sendValueInWebDriverWait('/html/body/app-providerportal/div/div/app-login/div/verify-identity/form/div[4]/div[4]/div[2]/div[1]/div[2]/input', 10, "Mysore")

    #security question 2
    sendValueInWebDriverWait('/html/body/app-providerportal/div/div/app-login/div/verify-identity/form/div[4]/div[4]/div[2]/div[2]/div[2]/input', 10, "Bangalore")

    # click on login button
    clickByWebDriverWait('/html/body/app-providerportal/div/div/app-login/div/verify-identity/form/div[5]/button', 15)

    bodies = get_response_bodies(driver, "https://authservice.caloptima.org/api/v1/ProviderAuth/getToken")
    bearerToken = bodies[0]["access_token"]

    driver.quit()
    # The JSON body/data to be sent with the request

    excel_data = pd.read_excel('Cal-Optima Test Data.xlsx')
    data_as_list = excel_data.to_dict(orient='records')

    print('Eligibility')
    for value in data_as_list:
        print(value['policy_number'])
        data = {
            "memberId": value['policy_number'],
            "isInternalUser": False,
            "userName": "asfan.s@rsbhealthcareconsulting.com",
            "providerCollectionId": 11042
        }
        responseEle= callCaloptima(bearerToken, data)
        print('==========================================================================================')
        print('claims')
        claims_data = {
            "startDate": one_year_back_timestamp,
            "endDate": timestamp,
            "status": ["In Progress", "Check Pending", "Finalized", "Original Claim"],
            "cin": value['policy_number'],
            "dateFilter": "DateOfService",
            "username": "asfan.s@rsbhealthcareconsulting.com",
            "sortAscending": False,
            "sortColumn": "dateOfService",
            "adtFacilityName": "",
            "adtType": "DateOfService",
            "adtStatus": "",
            "adtSubtype": [],
            "pageNumber": 1,
            "pageSize": 20,
            "providerCollectionId": 11042
        }
        response = callCaloptimaGetProviderClaimsByCriteria(claims_data)
        dict = {}
        try :
            if response and 'items' in response and len(response['items']) > 0:
                dict.update(response['items'][0])
            if responseEle and len(responseEle) > 0:
                dict.update(responseEle[0])
            dataListResponse.append(dict)
        except Exception as e:
            print("Error for ", value['policy_number'])

     #insert list in XlFiles
    print(dataListResponse)
    df = pd.json_normalize(dataListResponse, sep='_')
    df.to_excel(output_filename, index=False)

except Exception as e:
    print("Error:", str(e))
finally:
    pass
    # Continue with your automation or clean up

