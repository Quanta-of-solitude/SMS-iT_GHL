# SMS-iT_GHL
Integrating SMS-iT Decentralized Gateway API to send messages(SMS) from GHL
> This is just being used to send messages using the Conversations API of GHL, by integrating SMS-iT to the GHL account.


- [Installation](#installation)
  * [Dependencies](#dependencies)


<br />


### Installation
---
This has been written on Python 3 (used Python 3.7)

Once Python 3 and pip (Python Package Manager) is installed, clone the repository

```
git clone https://github.com/Quanta-of-solitude/SMS-iT_GHL.git
```

>Install Virtual Environment:

```
pip install virtualenv
```
in some cases if pip is not recognized use:

```
python -m pip install virtualenv
OR
python3 -m pip virtualenv
```
>cd to the cloned repository and 

Activate the virtual environment with:
```
python OR python3 -m venv env
source env/bin/activate
```
Run the following:
In some cases the pip requires an update:

```
pip install --upgrade pip
pip install wheel pybind11

pip install -r requirements.txt
```
### Dependencies:
1. flask
2. requests
3. ujson

Use [Ngrok](https://ngrok.com/) to setup a forwardingg tunnel at port 5000

Inside the folder configs/
Put your credentials in the fields assigned.

<br />

### Run the flask server:
 
 ```
 python app.py
 ```
 
> This will begin the server running at port 5000
 
Also, run ngrok at port 5000.
<br />

### GHL Marketplace Setup

In your created app, go to SMS providers and add the generated ngrok link with /smsit_sms as endpoint.
Example: 123ascf.dase.ngrok.io/smsit_sms

Once done and the app is authorized, we can use the the conversations API within GHL to send message to a contact or message a contact through GHL appointments diretly through SMS-iT.

> more to be updated.
