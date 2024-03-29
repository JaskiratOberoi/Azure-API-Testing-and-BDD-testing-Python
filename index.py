import requests
import json


# To gain access token without postman


def get_access_token(self):
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


# Calling the Access token function and saving the generated access token into a string.

access_token = get_access_token('self')

# API definitions
subId = "eee987ce-8b13-4971-b0e2-43856270922f"

url = "https://management.azure.com/subscriptions?api-version=2016-06-01"
url2 = 'https://management.azure.com/subscriptions/'+subId+'/resourcegroups?api-version=2017-05-10'
headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + access_token
}

# API Call using the Access token for Subscription Info API
response = requests.get(url=url, headers=headers)
Database = response.json()["value"]

# API Call using the Access token for Resource Groups API
responseRG = requests.get(url=url2, headers=headers)
ResourceG = responseRG.json()["value"]

# Information received from the Resource Group API
def resource_group_response():
    print(responseRG)
    for i in range(0, len(ResourceG)):
        print("Resource Group Name : " + ResourceG[i]["name"])
        print("Resource Group Location : " + ResourceG[i]["location"] + "\n")




# Information received from the Sub ID API
def print_response():
    print(response)
    state = input("Enter State of Subscription : ")
    for i in range(0, len(Database)):
        if Database[i]["state"] == state:
            print("Display Name of Subscription : " + Database[i]["displayName"])
            print("Subscription ID of Account : " + Database[i]["subscriptionId"])
            print("State of the Subscription [Enabled/Disabled] : " + Database[i]["state"])

# print_response()
# resource_group_response()