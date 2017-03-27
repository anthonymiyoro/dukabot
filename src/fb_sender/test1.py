import requests
import json
import uuid
from datetime import datetime
nowtime = str(datetime.now())

def buy(sender_msisdn, recipient_msisdn):
    url = "https://vitelco-demo.jumo.world/transactions/"
    headers={"Authorization":"8e974ff7fd1428fc8ba5ac912002ff8c", "DATE":nowtime, "Content-Type":"application/json", "X-CorrelationID":str(uuid.uuid4())}

    payload = {
        "amount": "2000",
        "currency": "KSH",
        "type": "merchantPayment",
        "requestDate": nowtime,
        "requestingOrganisationTransactionReference": "MWCAPIWorkshop001",
        "debitParty": [
        {
        "key": "msisdn",
        "value": sender_msisdn
        }
        ],
        "creditParty": [
        {
        "key": "msisdn",
        "value": recipient_msisdn
        }
    ]
}
    response = requests.post(url=url, headers=headers, data=json.dumps(payload))
    return response

buy_response =  buy('+254720000802', '+254720000800')
print (buy_response.text)