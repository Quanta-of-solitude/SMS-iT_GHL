import ujson as json 

##Just load tokens normal relative
def load_tokens():
    ##Load tokens
    with open("./configs/config.json") as cred:
        creds = json.load(cred)
    return creds 

