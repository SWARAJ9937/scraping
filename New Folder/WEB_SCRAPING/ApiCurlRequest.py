import requests
import json

# URL to which the request will be sent
url = "https://authservice.caloptima.org/api/v1/ProviderAuth/login"
# Cookies Global
cookies = {
    'RRAffinity': '939fcd7dd9fa28a0de8e3fc43ab7c67d4b2e22ac6b87f7aec0bc76031ca9f825',
    'ARRAffinitySameSite': '939fcd7dd9fa28a0de8e3fc43ab7c67d4b2e22ac6b87f7aec0bc76031ca9f825',
    'TS01412f5f': '011ec5726e7c2831e3fd32469229c1b116226bdf49dcd9efc30427cdba25858aa8f7c496d9f79be39c1fd8e7bc7106a0968ac8eff4',
    'TS019f299d': '011ec5726e7c2831e3fd32469229c1b116226bdf49dcd9efc30427cdba25858aa8f7c496d9f79be39c1fd8e7bc7106a0968ac8eff4'
}
# Headers extracted from the curl command
headers = {
    "Accept": "application/json, text/plain, */*",
    # "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
    # "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://provider.caloptima.org",
    "Referer": "https://provider.caloptima.org/",
    # "Sec-Fetch-Dest": "empty",
    # "Sec-Fetch-Mode": "cors",
    # "Sec-Fetch-Site": "same-site",
    # "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "identifier": "17130894151120.19189319933937066",
    # "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
    # "sec-ch-ua-mobile": "?0",
    # "sec-ch-ua-platform": "Linux"
}

# JSON data to be sent with the request
data = json.dumps({
    "userName": "asfan.s@rsbhealthcareconsulting.com",
    "password": "Rsb@123",
    "clientId": "1c0cda4a2aa14a05b94f42afbb73931e"
})

# Step 2: Make the Request
response = requests.post(url, headers=headers, data=data, cookies=cookies)
print("Login Response Text:", response.text)
print("Login Response Status Code:", response.status_code)
print("Login Response Cookies:", response.cookies)
#  ==========================  Login Success =========================================
#  ==========================  Factors =========================================


#Factors
requestCookie = "; ".join(f"{key}={value}" for key, value in response.cookies.items())
print("\nrequestCookiesn- 1: ", requestCookie) #todo Remove this line in future
print("\nformatedCookie- 1: ", response.cookies) #todo Remove this line in future
headers_factors = {
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "Cookie": requestCookie,
    # "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
    # "Connection": "keep-alive",
    "Origin": "https://provider.caloptima.org",
    "Referer": "https://provider.caloptima.org/",
    # "Sec-Fetch-Dest": "empty",
    # "Sec-Fetch-Mode": "cors",
    # "Sec-Fetch-Site": "same-site",
    # "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "identifier": "17130894151120.19189319933937066",
    # "sec-ch-ua": '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    # "sec-ch-ua-mobile": "?0",
    # "sec-ch-ua-platform": "Linux",
}

# URL for the next API endpoint
url_factors = "https://authservice.caloptima.org/api/v1/ProviderAuth/factors"
# Make the second request using the same session cookies
response_factors = requests.get(url_factors, headers=headers_factors, cookies=response.cookies)
print("Factors Response Text:", response_factors.text)
print("Factors Response Status Code:", response_factors.status_code)
print("Factors Response Cookies:", response_factors.cookies)
print("\n")

#  ==========================  Get Factors Success =========================================
#  ==========================  authenticate Factors =========================================

# requestCookie = "Cookie: .AspNetCore.Session=CfDJ8FS2YGrLtlhEkXLaDS7DahWVQiWS3TgfX%2Fywu6CcrUBI9%2Fy97W81RdSZQGDaXr0Po2KXIH50L8hjmX1UyBCNggZ9p1fbGt9cLxzE9AR%2BcwMFr6OPH8%2BFHcU5G8YcjF9c0Azw3ksvlEqlxA3VANRlL7G3ZxUQiW65rHuiyQ8QZ62G; ARRAffinity=939fcd7dd9fa28a0de8e3fc43ab7c67d4b2e22ac6b87f7aec0bc76031ca9f825; ARRAffinitySameSite=939fcd7dd9fa28a0de8e3fc43ab7c67d4b2e22ac6b87f7aec0bc76031ca9f825; TS0122f043=011ec5726efb3d71cbc87ccbe108a0316f34dbe923d161ed5a78e4598f591b466065537f3ac71829a3bb3270337a6ebcbe16f4cc31; TS0122f043=011ec5726e9694203daf5ec9cd876e8e654f3ae378755d2ee0686bc204ba3bf703ded0795a9d717deb4805b4fcbb52da0f46d29439"#.join(f"{key}={value}" for key, value in response_factors.cookies.items())
print("requestCookies-2: ", requestCookie)
authServiceHeaders = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7,zh-CN;q=0.6,zh;q=0.5",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Cookie": requestCookie,#'ARRAffinity=939fcd7dd9fa28a0de8e3fc43ab7c67d4b2e22ac6b87f7aec0bc76031ca9f825; ARRAffinitySameSite=939fcd7dd9fa28a0de8e3fc43ab7c67d4b2e22ac6b87f7aec0bc76031ca9f825; TS0122f043=011ec5726e355e2da780199b893192b41698df8533e103c9564cf45d4755cecca61272151b75a5672b5835642b00716ba499b9ffd3; .AspNetCore.Session=CfDJ8FS2YGrLtlhEkXLaDS7DahVgGpC78ECHZZopMvifVXCXa%2FZvoZ1BCcLcXpky1brOdynbq3wO6WbRK9iFj5OhFaqYtPYxcDa89OFLM8VRcdl9nnKqbRpqZCVvaacbKStmZ9iGfI3SmPu0oYm2JZ%2FZ77cIG81PEaHa194R05pe21nd; TS0122f043=011ec5726e8b913410a64ce379f236631e373a9eda73e17ca647c6c5b9a7792abd0a3bbe023ce566fa26ca71a0b422c6ab175ee34f".
    "Origin": "https://provider.caloptima.org",
    "Referer": "https://provider.caloptima.org/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "identifier": "17131021720270.3652664556482832",
    "sec-ch-ua": '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Linux",
}


# authservice
authServiceUrl = "https://authservice.caloptima.org/api/v1/ProviderAuth/authenticateFactors"

# Data to be sent with the request
authServiceData = [
    {"factorType": "Question", "factorID": "KBQ1", "value": "Mysore"},
    {"factorType": "Question", "factorID": "KBQ2", "value": "Bangalore"}
]

print("authServiceHeaders: ", authServiceHeaders)

# Make the POST request
authServiceResponse = requests.post(authServiceUrl, headers=authServiceHeaders, json=authServiceData, cookies=response.cookies)

# Print the response status code and body
print("Status Code:", authServiceResponse.status_code)
print("Response Body:", authServiceResponse.text)
