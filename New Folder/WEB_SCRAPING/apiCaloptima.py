import requests
import json


def callCaloptima():
    # The URL to which the request is being sent
    url = 'https://providerservice.caloptima.org/api/member/getMembersById'

    # Headers as specified in the curl request
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
        'Access-Control-Request-Headers': 'authorization,content-type,identifier',
        'Access-Control-Request-Method': 'POST',
        'Connection': 'keep-alive',
        'Origin': 'https://provider.caloptima.org',
        'Referer': 'https://provider.caloptima.org/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsIng1dCI6ImJlNXAtcHpmUTRFRGw4bHVjTjFVZ1NYOFpZUSIsImtpZCI6ImJlNXAtcHpmUTRFRGw4bHVjTjFVZ1NYOFpZUSIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIxNjU3ZmViNGM4NmU0NTE4YjFhNjM1MTFmMjA1MjliOSIsImNsaWVudF9pZCI6IjFjMGNkYTRhMmFhMTRhMDViOTRmNDJhZmJiNzM5MzFlIiwic2NvcGUiOlsiZW1haWwiLCJnYWxsZXJ5bWFuYWdlbWVudCIsIm9mZmxpbmVfYWNjZXNzIiwib3BlbmlkIiwicHJvZmlsZSJdLCJzdWIiOiJhc2Zhbi5zQHJzYmhlYWx0aGNhcmVjb25zdWx0aW5nLmNvbSIsImF1dGhfdGltZSI6MTcxMjY0ODQ2OCwiaWRwIjoiU2VjdXJlQXV0aDEyIiwiYW1yIjpbInBhc3N3b3JkIl0sIm5iZiI6MTcxMjY0ODQ2OCwiZXhwIjoxNzEyNjc3MjY4LCJpc3MiOiJodHRwczovL21lbWJlci5jYWxvcHRpbWEub3JnIiwiYXVkIjoiaHR0cHM6Ly9tZW1iZXIuY2Fsb3B0aW1hLm9yZyJ9.RNuCRyWFZ8xaLFF3CFIYnGIsL8hJiyzk8Q7F2wK4aW-ua0_iW24QjhP9Ud5QrBjGIHxATaFiq3yojjyzHJlkldv04q6mNN-RaVMsDEwYyIgq-vXoYj5Xl5-ghWH6nQyUxUmQgEwqH1thXD1MThlXp1rOdgcQ8ER8Y8zAQam_0CDJeSA6Inc4UVci10xsGTX39tqrNd0hiyHEDC7rrTBeyelw0Zs9w3CHEGvXFsJF8tznn4FuhU_IQ-DKU8pVZh6vkvadpTACnlXcY-f5KAGjvemsOpHbcPWv9sbpYggQ-DsqyY1RQDXvRSNwH9km0yFw8xan1Jmc0SeSPul8piV91A',
        'Content-Type': 'application/json',
        'Cookie': 'ARRAffinity=939fcd7dd9fa28a0de8e3fc43ab7c67d4b2e22ac6b87f7aec0bc76031ca9f825; ARRAffinitySameSite=939fcd7dd9fa28a0de8e3fc43ab7c67d4b2e22ac6b87f7aec0bc76031ca9f825; TS01400915=011ec5726ed58c60e801ee17fda2bdfa8cad3b344f6e0ed3d393e66aca13723ab2901e14973272ffb598adf35584a20ee1c347eb6e; TS019f299d=011ec5726e5ca146098d073b86706cdc8381d1e615a678077d3174665799a8c528503cdb9d1bc7306686a8d9314ab8eddbd214ee1c; TS019f299d=011ec5726ee5690c4ab426f74f9d7c4db87ee4e1829edd7dd1b389ff2c844a8e125d7371f2429e0af9515a32f3c49f2c7eccb341c3',
        'identifier': '17124829179990.23228819479715557',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"'
    }

    # The JSON body/data to be sent with the request
    data = {
        "memberId": "96942801g",
        "isInternalUser": False,
        "userName": "asfan.s@rsbhealthcareconsulting.com",
        "providerCollectionId": 11042
    }

    # Making the POST request
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Checking the response and printing accordingly
    if response.status_code == 200:
        print("Request was successful.")
        print(response.json())
    else:
        print(f"Request failed with status code: {response.status_code}")

      
def callCaloptimaGetProviderClaimsByCriteria():  
    url = 'https://providerservice.caloptima.org/api/claim/getProviderClaimsByCriteria'

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
        'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsIng1dCI6ImJlNXAtcHpmUTRFRGw4bHVjTjFVZ1NYOFpZUSIsImtpZCI6ImJlNXAtcHpmUTRFRGw4bHVjTjFVZ1NYOFpZUSIsInR5cCI6IkpXVCJ9.eyJpZHAiOiJTZWN1cmVBdXRoMTIiLCJhdXRoX3RpbWUiOjE3MTI0NzU0NzMsImFtciI6WyJwYXNzd29yZCJdLCJzdWIiOiJhc2Zhbi5zQHJzYmhlYWx0aGNhcmVjb25zdWx0aW5nLmNvbSIsImZhbWlseV9uYW1lIjoiQWhtZWQiLCJnaXZlbl9uYW1lIjoiQXNmYW4iLCJlbWFpbCI6ImFzZmFuLnNAcnNiaGVhbHRoY2FyZWNvbnN1bHRpbmcuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImp0aSI6IjI4MGY0NDc2MzRhZjRkNTVhOWJlN2M2YzFmY2M3NDk2Iiwibm9uY2UiOiIyNnNXWTZtSGg3OG5yNDZKOUlEek9QV292dzJyUGdkOExscGlES21ZIiwiYXRfaGFzaCI6IlJSQ040aHpCOFZVWjA0cWtzVFdpTEEiLCJpYXQiOjE3MTI0NzU0NzMsIm5iZiI6MTcxMjQ3NTQ3MywiZXhwIjoxNzEyNTA0MjczLCJpc3MiOiJodHRwczovL21lbWJlci5jYWxvcHRpbWEub3JnIiwiYXVkIjoiMWMwY2RhNGEyYWExNGEwNWI5NGY0MmFmYmI3MzkzMWUifQ.Ex5q3BGrNqiJOMs2idJtnF1SIy81qI8edLUn0SeUCcdlcvLiCtdnVIcUvBsoyTxRCw9GLohD5SCOhqg6Wcyd-P7fdhjZRenyQlu_TrXKqpFdHimPF0qMYAfCFMeAetq63xq4hanVoPxz-t_GzDjoytT0YNQ_ZjJzUcwGzwfE8BOHADm9wS8P74VUYMZSt3H-J99rT9PKz9_C6joWTNuoMUqClk6hMojI_y41br4adgimceXrnI3NimrpviDLWY7dWq4pNg0vchnL7p84O4Ah3w9DhtTmLlVI9YNr8haPmZN4UxGt861jq9DBiXDSzY30AX8JhLc1AsvZeFNGTApMUg',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Cookie': 'ARRAffinity=939fcd7dd9fa28a0de8e3fc43ab7c67d4b2e22ac6b87f7aec0bc76031ca9f825; ARRAffinitySameSite=939fcd7dd9fa28a0de8e3fc43ab7c67d4b2e22ac6b87f7aec0bc76031ca9f825; TS019f299d=011ec5726ed58c60e801ee17fda2bdfa8cad3b344f6e0ed3d393e66aca13723ab2901e14973272ffb598adf35584a20ee1c347eb6e; TS01400915=011ec5726ed58c60e801ee17fda2bdfa8cad3b344f6e0ed3d393e66aca13723ab2901e14973272ffb598adf35584a20ee1c347eb6e; TS019f299d=011ec5726e650f2c188f0d729b3b5d8f9a682c6cdfbbd2e10c30c4bc13b722b6ce19a4fe47fa0e6b6480c816b569f907db60c98c2f',
        'Origin': 'https://provider.caloptima.org',
        'Referer': 'https://provider.caloptima.org/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'identifier': '17124667353440.1779999597943962',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
    }

    claims_data = {
        "startDate": "2024-01-07T05:14:50.205Z",
        "endDate": "2024-04-07T05:14:50.205Z",
        "status": ["In Progress", "Check Pending", "Finalized", "Original Claim"],
        "cin": "96942801g",
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

    response = requests.post(url, headers=headers, data=json.dumps(claims_data))
    if response.status_code == 200:
        print("Request was successful.")
        print(response.json())
    else:
        print("Request failed with status code:", response.status_code)


callCaloptima()
print("====")
callCaloptimaGetProviderClaimsByCriteria()
