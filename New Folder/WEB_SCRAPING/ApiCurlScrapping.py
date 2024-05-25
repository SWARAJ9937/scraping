import requests

# Define the URL and endpoint
url = 'https://authservice.caloptima.org/api/v1/ProviderAuth/getToken'

# Define the headers
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Cookie': 'ARRAffinity=939fcd7dd9fa28a0de8e3fc43ab7c67d4b2e22ac6b87f7aec0bc76031ca9f825; ARRAffinitySameSite=939fcd7dd9fa28a0de8e3fc43ab7c67d4b2e22ac6b87f7aec0bc76031ca9f825; .AspNetCore.Session=CfDJ8FS2YGrLtlhEkXLaDS7DahWG1tqSu%2FTFncPL5QzILWdgOtiKtBYnzqMGwVpt41gVkWxv9zYAeCl9fWZ3K1F6cCdqbK6Mui97dF3yH5QPmLaiUGyOi3ExPyjCyihyic9I3%2BBEVyUQ6lkhNcpZTZio3tTY9TRY0V6SI6g5fXoVXZGK; TS0122f043=011ec5726ebddae9f12a2a58847615c41bd69fe6a4adefae91cc987d34f68a57c5b3c9fcd18c45eb37602f9816ba1a6a1b08ec434c; TS0122f043=011ec5726e1657971a85cbbaa6215d3b25c763c86878246c46e00d79a003d8e0a64d9f9b9acb34a7ba127295786a5e3fc925ae360b',
    'Origin': 'https://provider.caloptima.org',
    'Referer': 'https://provider.caloptima.org/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'identifier': '17130115545070.3896458557119631',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"'
}

# Define the JSON data payload
data = {
    "clientID": "1c0cda4a2aa14a05b94f42afbb73931e",
    "redirectUri": "https://provider.caloptima.org/",
    "scopes": [
        "openid",
        "profile",
        "email",
        "offline_access",
        "gallerymanagement"
    ],
    "nonce": "1LM6VW4UacWAi3oasU4B85BWklkaMxQAgkPshrl7",
    "remember": False
}

# Make the POST request
response = requests.post(url, headers=headers, json=data)
response_json = response.json()
access_token = response_json.get('access_token', 'No access token provided')

