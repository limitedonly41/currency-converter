
import datetime
from flask import Flask, render_template, request, redirect, url_for, flash

import pytz # $ pip install pytz


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

import requests


def get_usdt(rub):
    
    headers = {
        'authority': 'p2p.binance.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'bnc-uuid': '89e108b3-18aa-41d5-a712-09e5a9b3ad57',
        'c2ctype': 'c2c_merchant',
        'clienttype': 'web',
        'content-type': 'application/json',
        # 'cookie': 'cid=Sdp662bU; bnc-uuid=89e108b3-18aa-41d5-a712-09e5a9b3ad57; source=organic; campaign=www.google.com; _gid=GA1.2.1032945398.1672698375; fiat-prefer-currency=UZS; _gcl_au=1.1.2120912856.1672698375; BNC_FV_KEY=33d7e653797da8e4978b5d9c1a9c3df7d4fe08fe; OptanonAlertBoxClosed=2023-01-02T22:26:19.108Z; _gaexp=GAX1.2.9CLXk82vROyVycfKM9GOzA.19434.1; se_sd=BJQFhAgcRRXBhYXoEUgcgZZUgCxIMEVW1tT9QUUZVNSWgFlNXVwA1; se_gd=w0aUxDx8bGGWAAJcVWwAgZZERDA4MBVW1sW9QUUZVNSWgFVNXVQd1; se_gsd=UTQ0LDN9IyU2GVoBNxwnFVMEClYUAAoYUl9GWlxaVFNUElNS1; s9r1=5E9F0CA7A2D63A9965457623FA4E9DA3; BNC-Location=BINANCE; userPreferredCurrency=RUB_USD; userQuoteAsset=BTC; theme=dark; sys_mob=no; lang=ru; cr00=E333C2108CB2D5EB83FEFC873B04D95B; d1og=web.553450359.2EAC06648E31D61CF81E701F3AFBDFFD; r2o1=web.553450359.9F6343CD268FD4DF485CDEC538AC7E06; f30l=web.553450359.8B01D2F9587C80F9340676BC1E7EE1FD; logined=y; isAccountsLoggedIn=y; __BNC_USER_DEVICE_ID__={"1838615893306801cea3360e26be4393":{"date":1672789339458,"value":"1672789339251yVh5lfD0Ka7cHST7ZFp"}}; p20t=web.553450359.75DDF086F5A6F79D55ECCFC3BB129FF6; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22553450359%22%2C%22first_id%22%3A%221857497ad70163e-0707ddb9e842dcc-17525635-1296000-1857497ad711abe%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg1NzQ5N2FkNzAxNjNlLTA3MDdkZGI5ZTg0MmRjYy0xNzUyNTYzNS0xMjk2MDAwLTE4NTc0OTdhZDcxMWFiZSIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjU1MzQ1MDM1OSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22553450359%22%7D%2C%22%24device_id%22%3A%221857497ad70163e-0707ddb9e842dcc-17525635-1296000-1857497ad711abe%22%7D; _gat=1; _gat_UA-162512367-1=1; BNC_FV_KEY_EXPIRE=1672827764571; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Jan+04+2023+05%3A22%3A50+GMT%2B0100+(%D0%A6%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.34.0&isIABGlobal=false&hosts=&consentId=8a579ee9-1a29-43e7-b89b-96a3896e84de&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&geolocation=PL%3B14&AwaitingReconsent=false; showBlockMarket=false; _ga=GA1.2.9017812.1672698375; common_fiat=RUB; _ga_3WP50LGEEC=GS1.1.1672806164.5.1.1672806188.36.0.0',
        'csrftoken': '1b481738d97c6ab54fd339559f2b078b',
        'device-info': 'eyJzY3JlZW5fcmVzb2x1dGlvbiI6IjkwMCwxNDQwIiwiYXZhaWxhYmxlX3NjcmVlbl9yZXNvbHV0aW9uIjoiOTAwLDE0NDAiLCJzeXN0ZW1fdmVyc2lvbiI6Ik1hYyBPUyAxMC4xNS43IiwiYnJhbmRfbW9kZWwiOiJ1bmtub3duIiwic3lzdGVtX2xhbmciOiJydS1SVSIsInRpbWV6b25lIjoiR01UKzEiLCJ0aW1lem9uZU9mZnNldCI6LTYwLCJ1c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTVfNykgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwOC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwibGlzdF9wbHVnaW4iOiJQREYgVmlld2VyLENocm9tZSBQREYgVmlld2VyLENocm9taXVtIFBERiBWaWV3ZXIsTWljcm9zb2Z0IEVkZ2UgUERGIFZpZXdlcixXZWJLaXQgYnVpbHQtaW4gUERGIiwiY2FudmFzX2NvZGUiOiJlOWJiMDA4NiIsIndlYmdsX3ZlbmRvciI6Ikdvb2dsZSBJbmMuIChBcHBsZSkiLCJ3ZWJnbF9yZW5kZXJlciI6IkFOR0xFIChBcHBsZSwgQXBwbGUgTTEsIE9wZW5HTCA0LjEpIiwiYXVkaW8iOiIxMjQuMDQzNDQ5Njg0NzUxOTgiLCJwbGF0Zm9ybSI6Ik1hY0ludGVsIiwid2ViX3RpbWV6b25lIjoiRXVyb3BlL1dhcnNhdyIsImRldmljZV9uYW1lIjoiQ2hyb21lIFYxMDguMC4wLjAgKE1hYyBPUykiLCJmaW5nZXJwcmludCI6Ijk5MDNiM2Y4ZTRhYmUwNWY5NGZhMTczOTI3ZGI1YTM0IiwiZGV2aWNlX2lkIjoiIiwicmVsYXRlZF9kZXZpY2VfaWRzIjoiMTY3Mjc4OTMzOTI1MXlWaDVsZkQwS2E3Y0hTVDdaRnAifQ==',
        'fvideo-id': '33d7e653797da8e4978b5d9c1a9c3df7d4fe08fe',
        'lang': 'ru',
        'origin': 'https://p2p.binance.com',
        'referer': 'https://p2p.binance.com/ru/trade/all-payments/USDT?fiat=RUB',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'x-trace-id': 'd0865eac-2369-4060-8855-1df95f5428fb',
        'x-ui-request-trace': 'd0865eac-2369-4060-8855-1df95f5428fb',
    }


    json_data = {
        'proMerchantAds': False,
        'page': 1,
        'rows': 10,
        'countries': [],
        'publisherType': None,
        'fiat': 'RUB',
        'tradeType': 'BUY',
        'asset': 'USDT',
        'merchantCheck': False,
        'transAmount': f'{rub}',
    }
    response = requests.post(
        'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search',
        headers=headers,
        json=json_data,
    )

    return response.json()['data'][0]['adv']['price']

def sell_usdt(usdt):

    headers = {
        'authority': 'p2p.binance.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'bnc-uuid': '89e108b3-18aa-41d5-a712-09e5a9b3ad57',
        'c2ctype': 'c2c_merchant',
        'clienttype': 'web',
        'content-type': 'application/json',
        # 'cookie': 'cid=Sdp662bU; bnc-uuid=89e108b3-18aa-41d5-a712-09e5a9b3ad57; source=organic; campaign=www.google.com; _gid=GA1.2.1032945398.1672698375; fiat-prefer-currency=UZS; _gcl_au=1.1.2120912856.1672698375; BNC_FV_KEY=33d7e653797da8e4978b5d9c1a9c3df7d4fe08fe; OptanonAlertBoxClosed=2023-01-02T22:26:19.108Z; _gaexp=GAX1.2.9CLXk82vROyVycfKM9GOzA.19434.1; se_sd=BJQFhAgcRRXBhYXoEUgcgZZUgCxIMEVW1tT9QUUZVNSWgFlNXVwA1; se_gd=w0aUxDx8bGGWAAJcVWwAgZZERDA4MBVW1sW9QUUZVNSWgFVNXVQd1; se_gsd=UTQ0LDN9IyU2GVoBNxwnFVMEClYUAAoYUl9GWlxaVFNUElNS1; s9r1=5E9F0CA7A2D63A9965457623FA4E9DA3; BNC-Location=BINANCE; userPreferredCurrency=RUB_USD; userQuoteAsset=BTC; theme=dark; sys_mob=no; lang=ru; cr00=E333C2108CB2D5EB83FEFC873B04D95B; d1og=web.553450359.2EAC06648E31D61CF81E701F3AFBDFFD; r2o1=web.553450359.9F6343CD268FD4DF485CDEC538AC7E06; f30l=web.553450359.8B01D2F9587C80F9340676BC1E7EE1FD; logined=y; isAccountsLoggedIn=y; __BNC_USER_DEVICE_ID__={"1838615893306801cea3360e26be4393":{"date":1672789339458,"value":"1672789339251yVh5lfD0Ka7cHST7ZFp"}}; p20t=web.553450359.75DDF086F5A6F79D55ECCFC3BB129FF6; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22553450359%22%2C%22first_id%22%3A%221857497ad70163e-0707ddb9e842dcc-17525635-1296000-1857497ad711abe%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg1NzQ5N2FkNzAxNjNlLTA3MDdkZGI5ZTg0MmRjYy0xNzUyNTYzNS0xMjk2MDAwLTE4NTc0OTdhZDcxMWFiZSIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjU1MzQ1MDM1OSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22553450359%22%7D%2C%22%24device_id%22%3A%221857497ad70163e-0707ddb9e842dcc-17525635-1296000-1857497ad711abe%22%7D; BNC_FV_KEY_EXPIRE=1672827764571; showBlockMarket=false; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Jan+04+2023+05%3A37%3A51+GMT%2B0100+(%D0%A6%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.34.0&isIABGlobal=false&hosts=&consentId=8a579ee9-1a29-43e7-b89b-96a3896e84de&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&geolocation=PL%3B14&AwaitingReconsent=false; _ga=GA1.2.9017812.1672698375; _gat_UA-162512367-1=1; common_fiat=PLN; _ga_3WP50LGEEC=GS1.1.1672806164.5.1.1672807308.33.0.0',
        'csrftoken': '1b481738d97c6ab54fd339559f2b078b',
        'device-info': 'eyJzY3JlZW5fcmVzb2x1dGlvbiI6IjkwMCwxNDQwIiwiYXZhaWxhYmxlX3NjcmVlbl9yZXNvbHV0aW9uIjoiOTAwLDE0NDAiLCJzeXN0ZW1fdmVyc2lvbiI6Ik1hYyBPUyAxMC4xNS43IiwiYnJhbmRfbW9kZWwiOiJ1bmtub3duIiwic3lzdGVtX2xhbmciOiJydS1SVSIsInRpbWV6b25lIjoiR01UKzEiLCJ0aW1lem9uZU9mZnNldCI6LTYwLCJ1c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTVfNykgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwOC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwibGlzdF9wbHVnaW4iOiJQREYgVmlld2VyLENocm9tZSBQREYgVmlld2VyLENocm9taXVtIFBERiBWaWV3ZXIsTWljcm9zb2Z0IEVkZ2UgUERGIFZpZXdlcixXZWJLaXQgYnVpbHQtaW4gUERGIiwiY2FudmFzX2NvZGUiOiJlOWJiMDA4NiIsIndlYmdsX3ZlbmRvciI6Ikdvb2dsZSBJbmMuIChBcHBsZSkiLCJ3ZWJnbF9yZW5kZXJlciI6IkFOR0xFIChBcHBsZSwgQXBwbGUgTTEsIE9wZW5HTCA0LjEpIiwiYXVkaW8iOiIxMjQuMDQzNDQ5Njg0NzUxOTgiLCJwbGF0Zm9ybSI6Ik1hY0ludGVsIiwid2ViX3RpbWV6b25lIjoiRXVyb3BlL1dhcnNhdyIsImRldmljZV9uYW1lIjoiQ2hyb21lIFYxMDguMC4wLjAgKE1hYyBPUykiLCJmaW5nZXJwcmludCI6Ijk5MDNiM2Y4ZTRhYmUwNWY5NGZhMTczOTI3ZGI1YTM0IiwiZGV2aWNlX2lkIjoiIiwicmVsYXRlZF9kZXZpY2VfaWRzIjoiMTY3Mjc4OTMzOTI1MXlWaDVsZkQwS2E3Y0hTVDdaRnAifQ==',
        'fvideo-id': '33d7e653797da8e4978b5d9c1a9c3df7d4fe08fe',
        'lang': 'ru',
        'origin': 'https://p2p.binance.com',
        'referer': 'https://p2p.binance.com/ru/trade/sell/USDT?fiat=PLN&payment=SantanderPoland',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'x-trace-id': 'f74ea748-6a48-4cbe-864c-aa75e05750e8',
        'x-ui-request-trace': 'f74ea748-6a48-4cbe-864c-aa75e05750e8',
    }

    json_data = {
        'proMerchantAds': False,
        'page': 1,
        'rows': 10,
        'payTypes': [
            'SantanderPoland',
        ],
        'countries': [],
        'publisherType': None,
        'transAmount': f'{usdt}',
        'tradeType': 'SELL',
        'asset': 'USDT',
        'fiat': 'PLN',
        'merchantCheck': False,
    }

    response = requests.post(
        'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search',
        headers=headers,
        json=json_data,
    )

    return response.json()['data'][0]['adv']['price']

def main(rub):
    
    usdt = rub/float(get_usdt(rub))

    # print(usdt)
    
    pln = usdt*float(sell_usdt(usdt))
    # print(pln, '\n')
    
    rate = rub/pln
    # print('rate: ', rate)
    
    user_pln = rub/(rate*1.055) - 40
    
    user_rate = rub/user_pln
    app.logger.info(pln - user_pln,'_', rate)
    # print(pln - user_pln,'_', rate, file=sys.stderr)

    return user_pln, user_rate
    



@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    result = 0
    rate = 0
    date = datetime.datetime.now(pytz.timezone("Europe/Warsaw"))

    if request.method == 'POST':
        try:
            amount = int(request.form['amount'])
        except:
            amount = 50000

        if amount > 200_000:
            flash('Сумма должна быть меньше или равна 200 000 руб')
            return redirect(url_for('home'))

        if amount < 20_000:
            flash('Сумма должна быть больше или равна 20 000 руб')
            return redirect(url_for('home'))

        answer, rate = main(amount)
            
        return render_template('home.html', infos=['RUB'], out=['PLN'], rate=rate, result=answer, date=date, title="Home")
        
    return render_template('home.html', infos=['RUB'], out=['PLN'], rate=rate, result=result, date=date, title="Home")



if __name__ == '__main__':
    app.run(debug=True) # debug = False, in production
