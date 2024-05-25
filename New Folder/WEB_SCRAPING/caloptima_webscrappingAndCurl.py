from seleniumwire import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import gzip
import io

# Configure the Selenium Wire options to capture network traffic
seleniumwire_options = {
    'enable_har': True
}

screen_width = 1024
screen_height = 768

options = Options()
options.add_experimental_option("detach", True)
options.add_argument(f"--window-size={screen_width},{screen_height}")
service = Service(executable_path='./chromedriver')

# Initialize the WebDriver with Selenium Wire
driver = webdriver.Chrome(service=service, options=options, seleniumwire_options=seleniumwire_options)

def clickByWebDriverWait(value, timeOut):
    button = WebDriverWait(driver, timeOut).until(EC.element_to_be_clickable((By.XPATH, value)))
    button.click()

def sendValueInWebDriverWait(key, timeOut, value):
    input = WebDriverWait(driver, timeOut).until(
        EC.element_to_be_clickable((By.XPATH, key)))
    input.send_keys(value)

try :
    driver.get("https://provider.caloptima.org/#/login")

    # Your existing code to interact with the web page
    mail = 'asfan.s@rsbhealthcareconsulting.com'
    email_input_element = driver.find_element(By.ID, 'userName')
    email_input_element.send_keys(mail)

    pwd = 'Rsb@123'
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

    # Wait for a necessary network response or a specific timeout
    driver.wait_for_request('api/v1/ProviderAuth/getToken', timeout=30)

    # Iterate through the requests
    for request in driver.requests:
        if request.response and request.url == "https://authservice.caloptima.org/api/v1/ProviderAuth/getToken":
            print(f"URL: {request.url}")
            print("Status code:", request.response.status_code)

            content_type = request.response.headers.get('Content-Type', '')
            content_encoding = request.response.headers.get('Content-Encoding', '')

            # Handle based on Content-Encoding
            if 'gzip' in content_encoding:
                compressed_body = request.response.body
                if compressed_body:
                    decompressed_body = gzip.decompress(compressed_body)
                    if 'text' in content_type or 'json' in content_type:
                        print("Decompressed Response Body:", decompressed_body.decode('utf-8'))
                    else:
                        print("Decompressed Binary Data:", decompressed_body)
            else:
                if 'text' in content_type or 'json' in content_type:
                    print("Response Body:", request.response.body.decode('utf-8'))
                else:
                    print("Binary Data:", request.response.body)
except Exception as e:
    print("Error:", str(e))
finally:
    # Continue with your automation or clean up
    driver.quit()
