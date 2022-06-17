import requests
from collections import OrderedDict



class Send_Messages():

    def __init__(self,key,deviceID):
        self.endpoint = "https://www.smsit.ai/smsgateway/services/send.php"
        self.key = key
        self.deviceID = deviceID
    
    def send_sms_smsIT(self,data):
        #get contact phone 
        
        phone = data["phone"]
        message = data["message"]
        payload_2 = {
            'number': f'{phone}',
            'message': f'{message}',
            'key': f'{self.key}',
            'devices': self.deviceID, #my gateway device
            'type': 'sms',
            'prioritize': 0
        }
        # convert to Ordereddict
        data_x = OrderedDict(payload_2)
        response = requests.request("POST", self.endpoint,data=data_x)
        print("SMS-IT Response", response.json()) 



    