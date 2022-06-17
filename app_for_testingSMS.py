import ujson as json
import requests 
from flask import Flask, redirect, request, render_template
from func.ghl_token import GHL
import func.load_tokens as load_tokens 
import func.custom_conversations as converse



app = Flask(__name__)

ghl_functions = GHL()
messenger = converse.Send_Messages()

#Tokens Loaded
tokens = load_tokens.load_tokens()




#read the location from auth token file
def getv2credentials():
    with open("./ghlauth.json") as idfile:
        datafile = json.load(idfile)

    return datafile


@app.route('/')
def addAppGHL():
    link = f"https://marketplace.gohighlevel.com/oauth/chooselocation?response_type=code&redirect_uri={tokens['ngrok']}/callback&client_id={tokens['ghl_client_id']}&scope=locations/customFields.write%20contacts.readonly%20locations.readonly%20locations/customValues.readonly%20locations/tags.readonly%20locations/tags.write%20users.readonly%20conversations/message.write%20conversations/message.readonly"
	#return 'Hello World'
    #print(link)
    return redirect(link)



@app.route('/callback', methods=["POST","GET"])
def testback():
    print(request.url)
    strnIn = str(request.url).index('=')
    callback_code = str(request.url)[strnIn+1:]
    ghl_functions.ghl_createTk_auth(callback_code)
    
    return """Authenticated... you may close the window now"""


###SMS from SMS-it Testing Only
@app.route('/smsit_sms', methods=["POST","GET"])
def smstestonly():
    content_type = request.headers.get('Content-Type')
    data = request.json
    messenger.send_sms_smsIT(data)
    #print(data)
    return "OK"








# main driver function
if __name__ == '__main__':
    app.run(debug=True, port=5000, threaded = True)






