import os
import json
from twilio.rest import Client


ACCOUNT_SID = 'ACCOUNT_SID'
AUTH_TOKEN = 'AUTH_TOKEN'
NOTIFY_SERVICE_SID = 'NOTIFY_SERVICE_SID'
SERVICE_ID = 'SERVICE_ID'

client = Client(ACCOUNT_SID, AUTH_TOKEN)
client.notifications

def send_bulk_sms(numbers, body):
    bindings = list(map(lambda number: json.dumps({'binding_type': 'sms', 'address': number}), numbers))
    print("=====> To Bindings :>", bindings, "<: =====")
    notification = client.notify.services(SERVICE_ID).notifications.create(
        to_binding=bindings,
        body=body
    )
    print(notification.body)


def validate_body(data, required_fields):
    for field in required_fields:
        if field not in data:
            return False, field
    return True, None
    
