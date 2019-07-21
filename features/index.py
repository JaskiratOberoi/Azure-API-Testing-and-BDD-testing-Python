import requests
import json


# To gain access token without postman


def getaccesstoken(self):
    authority = 'https://login.microsoftonline.com/12d32f8e-676c-4c56-b178-5c3f80a0416c/oauth2/token'
    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }
    params = {
        'resource': 'https://management.azure.com/',
        'client_id': 'ca20ab31-7481-4bf2-b543-766efc2b245c',
        'grant_type': 'client_credentials',
        'tenantid': '12d32f8e-676c-4c56-b178-5c3f80a0416c',
        'client_secret': '1aRf23nYv1Y.nxnwECrZo?Tl@HSpj/=c'
    }
    response = requests.post(authority, data=params, headers=header)

    return json.loads(response.text)['access_token']


access_token = getaccesstoken('self')


subId = "eee987ce-8b13-4971-b0e2-43856270922f"
# url = 'https://management.azure.com/subscriptions/'+subId+'/resourcegroups?api-version=2017-05-10'
url = "https://management.azure.com/subscriptions?api-version=2016-06-01"
headers = {'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + access_token}



response = requests.get(url=url, headers=headers)
Database = dict()
Database = response.json()["value"]


print(response)
# print(Database)
state = input("Enter State of Subscription : ")

for i in range(0, len(Database)):
    if Database[i]["state"] == state:
        print("Display Name of Subscription : " + Database[i]["displayName"])
        print("Subscription ID of Account : " + Database[i]["subscriptionId"])
        print("State of the Subscription [Enabled/Disabled] : " + Database[i]["state"])


