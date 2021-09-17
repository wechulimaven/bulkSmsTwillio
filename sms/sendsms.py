import os
import json
from twilio.rest import Client

# +12053407016
ACCOUNT_SID = 'ACa14a9aefa34ec9fb7d09f640f4b453bc'
AUTH_TOKEN = '7ba356de67e8e6f069615d9fc5ef642f'
NOTIFY_SERVICE_SID = 'MG192a6b780cd9ba9d300bffbc0bcb403e'
SERVICE_ID = 'ISb144c6e9491541d8cb0f75a754e54990'

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
    