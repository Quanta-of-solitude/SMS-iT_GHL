import ujson as json 
import requests 
import func.load_tokens as load_tokens
from func.custom_conversations import Send_Messages


tokens = load_tokens.load_tokens()


#GHL Creds
GHL_Client_ID = tokens["ghl_client_id"]
GHL_Client_SECRET = tokens["ghl_client_secret"]



class GHL:
    
    def __init__(self):
        self.client_id = GHL_Client_ID
        self.client_secret = GHL_Client_SECRET



    def ghl_createTk_auth(self,code):
        url = "https://api.msgsndr.com/oauth/token"

        payload = f"client_id={self.client_id}&client_secret={self.client_secret}&grant_type=authorization_code&code={code}&refresh_token="
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.request("POST", url, data=payload, headers=headers)
        #print(response.content)
        
        with open("./ghlauth.json", "w") as outfile:
            outfile.write(json.dumps(response.json()))
        
        print("Oauth2 Token saved")



