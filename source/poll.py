import os

from dotenv import dotenv_values

from smtp.smtp import send_email

import json
import requests


def poll():
    env_path = os.path.join(os.getcwd(), "..", ".env")
    config = dotenv_values(env_path)
    # endpoint
    URL = "https://ttp.cbp.dhs.gov/schedulerapi/slot-availability"

    # location id
    locationId = config['LOCATIONID']

    PARAMS = {'locationId': locationId}

    r = requests.get(url=URL, params=PARAMS)

    try:
        active = json.loads(r.text)['availableSlots'][0]['active']
    except:
        active = 0

    if active:
        send_email(env_path)
        print("Slots available")
    else:
        print("No slots available")
