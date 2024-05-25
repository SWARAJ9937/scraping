import requests

# Set the URL
url = 'https://provider.healthnetcalifornia.com/careconnect/eligibility/check'

# Define the headers
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': ('JSESSIONID=93248359F944696C576ED06FF509EBE2.0d9mglk2nyshc41y; '
               'QSI_SI_8xnPDYmhumF6iKG_intercept=true; QSI_SI_6iqmsL9xPSWOqq2_intercept=true; '
               'dtCookie=v_4_srv_42_sn_DD3878C15273E1BDBC3882079D0380EF_perc_100000_ol_0_mul_1_app-3A7eaf0751440d4bd6_1; '
               'NSC_mc_qpsubm_qspwjefs_qspe=ffffffff090cbc7d45525d5f4f58455e445a4a4206cf; '
               'rxVisitor=1714217898970M7I10KV89NJJP1ABBT2KO9ILTBJ1K87R; '
               'NSC_oxfc6-443=ffffffff090c165945525d5f4f58455e445a4a42378b; '
               'evar16_s=Less than 1 day; s_vnc365=1745753899841&vn=16; s_ivc=true; '
               'AMCVS_E264EA7B5444D3850A4C98A1@AdobeOrg=1; '
               'AMCV_E264EA7B5444D3850A4C98A1@AdobeOrg=-637568504|MCIDTS|19841|MCMID|04181865537353538843565809268734628209|'
               'MCAAMLH-1714822699|12|MCAAMB-1714822699|RKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y|'
               'MCOPTOUT-1714225099s|NONE|MCAID|NONE|MCSYNCSOP|411-19847|vVersion|5.1.1; s_cc=true; '
               '__utma=194521708.833451016.1712151870.1714140682.1714217900.13; __utmb=194521708.0.10.1714217900; __utmc=194521708; '
               '__utmz=194521708.1714217900.13.12.utmcsr=sso.entrykeyid.com|utmccn=(referral)|utmcmd=referral|utmcct=/; '
               'dtSa=-; gvn_pn=provider%3Acareconnect%3Aeligibility%3Abulkchecker; evar16=1714218026900; '
               's_nr365=1714218026901-Repeat; SREINGRESS=ebee0f5826008ed0369dc2255a175dcb|a9de88e8e69080d6a3a3175a26b8e91f; '
               'RT="z=1&dm=healthnetcalifornia.com&si=218f0e9d-8684-4248-ab38-aa21f2a3de02&ss=lvi12n7h&sl=3&tt=b23&'
               'bcn=%2F%2F684d0d4c.akstat.io%2F&ld=2wdq&nu=p02ffwr&cl=4qy9"; rxvt=1714219914167|1714217898973; '
               'dtPC=42$18026253_654h10vVSVACBWPDAOTOFOEOUEQEVVUCRKBBROK-0e0; '
               'SREINGRESS=c724dbb72a8076c2dbcb8e6e71581460|701253fe67b78beac4431abb977f1b74'),
    'origin': 'https://provider.healthnetcalifornia.com',
    'priority': 'u=1, i',
    'referer': 'https://provider.healthnetcalifornia.com/careconnect/eligibility/bulkChecker',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-csrf-token': '061aef49-d372-43fc-b2e6-74dc3c386aa6',
    'x-dtpc': '42$18026253_654h10vVSVACBWPDAOTOFOEOUEQEVVUCRKBBROK-0e0',
    'x-requested-with': 'XMLHttpRequest'
}

# Define the data to be sent
data = {
    'dos': '01/18/2024',
    'memberIdOrLastName': '99256925G',
    'dob': '07/26/2019'
}

# Send POST request
response = requests.post(url, headers=headers, data=data)

# Print response
print(response.text)
