import requests

# Define the URL and headers based on the curl command
url = 'https://p-chcp.digitaledge.cigna.com/identity/profile/med/login-user-profile?consumerCode=1000'
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
    'authorization': 'Bearer eyJqa3UiOiJodHRwczovL2NpZ25hZm9yaGNwLmNpZ25hLmNvbS9tZ2Evc3BzL29hdXRoL29hdXRoMjAvandrcy9jaGNwX3NwYV9kZWYiLCJraWQiOiJHeURtNHR0Wk1ZUGs0bGRRTUEtU0VlWnpDU0l2OVd4VE5ieHFzY1pQX0JVIiwiYWxnIjoiUlMyNTYifQ.eyJpYXQiOjE3MTM0MzQ2OTksInN1YiI6ImNuPXNkaWxhYnMsb3U9cHJvdmlkZXJwZW9wbGUsbz1jaWduYS5jb20iLCJhdWQiOiJjaGNwX3NwYV9jbGllbnQiLCJodHRwczovL2NpZ25hZm9yaGNwLmNpZ25hLmNvbSI6eyJzZXNzaW9uSWQiOiI0MDIwYzkyYS1mZDY4LTExZWUtYTBlZi0wMDUwNTY4ZjA4NzIiLCJjbiI6InNkaWxhYnMiLCJlbmNyeXB0ZWRDbiI6IlZGWGV6OFUvYjM2UDh5emwzWlJxcWJiYTlZVjRBa2UrSXdyNlFMRHpIdEF2UDlwSXR1TmpsWGUwUW83V2drb0RXQjJmMzlTNUdpaEwwaXNIY3ZaSnpWTmNNQzlBWkplVmFPOHdwRkFFbHR5TkYvR3J2ZzRqbmNwZFk1RXA1K2VzOUlxUW1nLyt2OWdacmIrak1Rekx0QXBzZkRFT1RQK3grUHM5RE9uTGw5bz0iLCJsb2IiOiJNRUQiLCJjaGNwSWQiOiIxNTM1MDg0IiwiZW50aXRsZW1lbnRzIjpbIkRpcmVjdG9yeVVwZGF0ZXMiLCJFbnJvbGxBbmRNYW5hZ2VFRlQiLCJFT0NBY3Rpb25hYmxlUmVwb3J0aW5nIiwiQ2xhaW1zU2VhcmNoLVJlY29uc2lkZXJhdGlvbiIsIlByZWNlcnRpZmljYXRpb24iLCJQYXRpZW50UmVldmlld3NWaWV3Il19LAog...',
    'origin': 'https://cignaforhcp.cigna.com',
    'referer': 'https://cignaforhcp.cigna.com/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'Linux',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}
import json

# Sample JSON data as a string
json_data = '''
{
    "metadata": {
        "serviceReferenceId": "a6ccb582-174e-4db3-86ac-dfacdc4f6cf8",
        "outcome": {
            "status": 200,
            "type": "OK",
            "message": "Successful",
            "code": 0,
            "additionalDetails": []
        }
    },
    "user": {
        "ssoId": "sdilabs",
        "firstName": "Mano",
        "lastName": "Ganesan",
        "phone": "9793994966",
        "phoneExt": "",
        "email": "billing@sdilabsinc.com",
        "lob": "MED",
        "dob": "1985-07-23",
        "addressLine1": "12634 Hoover St",
        "addressLine2": "",
        "city": "Garden Grove",
        "state": "CA",
        "zip": "92841",
        "mobilePhone": "",
        "secPwdLastChangedDate": "2024-03-07",
        "lobPref": "CHCP",
        "emailVerified": "Y",
        "mobileVerified": "N",
        "isClaims360PopupSuppressed": "Y",
        "shouldShowWamOnboardingStatus": "false",
        "jobRole": "Billing/revenue cycle operations",
        "allEntitlements": [
            "PatientSearch",
            "ClaimsSearch",
            "RemittanceReports",
            "DirectoryUpdates",
            "EnrollAndManageEFT",
            "Precertification",
            "EOCActionableReporting",
            "PatientReviewsView",
            "ClaimsSearch-Reconsideration"
        ],
        "tins": {
            "954107792": {
                "entitlements": [
                    "PatientSearch",
                    "ClaimsSearch",
                    "RemittanceReports",
                    "DirectoryUpdates",
                    "EnrollAndManageEFT",
                    "Precertification",
                    "EOCActionableReporting",
                    "PatientReviewsView",
                    "ClaimsSearch-Reconsideration"
                ],
                "number": "954107792",
                "contracted": "Y",
                "sanctioned": false,
                "generatedTinId": "233260",
                "name": "SPECIALTY DIAGNOSTICS",
                "hasGovrnm": true,
                "hasComrcl": true,
                "lob": "MED"
            }
        },
        "permToggles": []
    }
}
'''

# Parse the JSON data into a Python dictionary
data = json.loads(json_data)

# Accessing user information
user_info = data['user']
print(f"Name: {user_info['firstName']} {user_info['lastName']}")
print(f"Email: {user_info['email']}")
print(f"Phone: {user_info['phone']}")
print(f"Date of Birth: {user_info['dob']}")

# Print some entitlements
print("User entitlements include:")
for entitlement in user_info['allEntitlements']:
    print(f"- {entitlement}")

# Accessing nested details in 'tins'
for tin, tin_details in user_info['tins'].items():
    print(f"TIN Number: {tin_details['number']}")
    print(f"Name: {tin_details['name']}")
    print(f"Contracted: {tin_details['contracted']}")
 

# Make the GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print("Request successful!")
    # Print the response text (JSON data)
    print(response.text)
else:
    print("Request failed")

