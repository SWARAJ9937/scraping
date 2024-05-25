import requests

url = "https://authservice.caloptima.org/api/v1/ProviderAuth/authenticateFactors"

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "identifier": "17132011745690.7461264434428523",
    "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Linux\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "cookie": "ARRAffinity=939fcd7dd9fa28a0de8e3fc43ab7c67d4b2e22ac6b87f7aec0bc76031ca9f825; ARRAffinitySameSite=939fcd7dd9fa28a0de8e3fc43ab7c67d4b2e22ac6b87f7aec0bc76031ca9f825; TS0122f043=011ec5726e37bf2af7926ae3e6ee1174821a601b788e06068aa1e29182ee4c650d1a415e921c971a9421281434ee2fa9b4dc238248; .AspNetCore.Session=CfDJ8FS2YGrLtlhEkXLaDS7DahXXGt8B6niH4DrmQIcAWEhWTxDJdXEsGd4Tl7XPKh1dQ%2FCqgk8IAOmDoVHcyWYl47lboZquasB%2BUXtTQcY6T%2B029EzdWisufQZVor5KiJh71OTEOXg6y22tOGRcMjSEO3SnwD5XYBi8oUSvKUqXHy7j",
    "Referer": "https://provider.caloptima.org/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}

data = [
    {"factorType": "Question", "factorID": "KBQ1", "value": "Mysore"},
    {"factorType": "Question", "factorID": "KBQ2", "value": "Bangalore"}
]

response = requests.post(url, headers=headers, json=data)

print(response.text)  # Print the response JSON
print(response.status_code)  # Print the response JSON
