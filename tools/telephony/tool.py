import requests

def send_sms_twilio(account_sid, auth_token, from_number, to_number, body):
    url = f'https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json'
    data = {
        'From': from_number,
        'To': to_number,
        'Body': body
    }
    try:
        resp = requests.post(url, data=data, auth=(account_sid, auth_token))
        if resp.status_code == 201:
            return 'SMS sent.'
        else:
            return f'Error: {resp.text}'
    except Exception as e:
        return str(e)
