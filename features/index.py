import requests
import json




# To gain access token without postman

def getaccesstoken(self):
 authority = 'https://login.microsoftonline.com/12d32f8e-676c-4c56-b178-5c3f80a0416c/oauth2/token'
 header = {'Content-Type': 'application/x-www-form-urlencoded',
 'Accept': 'application/json'
 }
 params = {
 'resource': 'https://management.azure.com/',
 'client_id': 'ca20ab31-7481-4bf2-b543-766efc2b245c',
 'grant_type': 'client_credentials',
 'tenantid': '12d32f8e-676c-4c56-b178-5c3f80a0416c',
 'client_secret': '1aRf23nYv1Y.nxnwECrZo?Tl@HSpj/=c'
 }
 response = requests.post(authority,data=params, headers=header)
 #sys.stdout.write(json.loads(response.text)['access_token'])
 return  json.loads(response.text)['access_token']

access_token = getaccesstoken('self')



subid = "eee987ce-8b13-4971-b0e2-43856270922f"
# access_token = """eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6InU0T2ZORlBId0VCb3NIanRyYXVPYlY4NExuWSIsImtpZCI6InU0T2ZORlBId0VCb3NIanRyYXVPYlY4NExuWSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuYXp1cmUuY29tLyIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzEyZDMyZjhlLTY3NmMtNGM1Ni1iMTc4LTVjM2Y4MGEwNDE2Yy8iLCJpYXQiOjE1NjM1MjI5NzMsIm5iZiI6MTU2MzUyMjk3MywiZXhwIjoxNTYzNTI2ODczLCJhaW8iOiI0MkZnWUxodyt2MHVqOThXUy9hc24xWitzYUIvQ1FBPSIsImFwcGlkIjoiY2EyMGFiMzEtNzQ4MS00YmYyLWI1NDMtNzY2ZWZjMmIyNDVjIiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvMTJkMzJmOGUtNjc2Yy00YzU2LWIxNzgtNWMzZjgwYTA0MTZjLyIsIm9pZCI6Ijc2MGM4YzExLTY3MGQtNDhkOS05NzUyLTllNDMxMTNkODQzNyIsInN1YiI6Ijc2MGM4YzExLTY3MGQtNDhkOS05NzUyLTllNDMxMTNkODQzNyIsInRpZCI6IjEyZDMyZjhlLTY3NmMtNGM1Ni1iMTc4LTVjM2Y4MGEwNDE2YyIsInV0aSI6Im9NYlFMQTNQeVU2NXc1RGZUemdnQUEiLCJ2ZXIiOiIxLjAifQ.iZfewZMQ6O0S8z1JNeOk6ipwl-WfUhSljsFkE43_KUpk9wpAv22dpzK8H6R-bz4iJ3tXcWvrw0FwkUTn7LZhmK0PRdr0OPQ-4TG1K-a9oO9JeqvsgtWKC5nd8AUT87Cvv6NtNs16oNI0lmyxVedTalN9UNwWMiBSV3Uo81PmRZuDYLzQCACXIdqxxq7so7XzffUB5q6ML64B2x7ctvHA_RpG6Vi7MemSBNDNzUcFmE43E_farfOuZHcHqDUIiPLtfG9Ebcl3JKp7wMdYEMHIKCKeg1n2XMKkU8DzNnE_P9XLqO0vcjSsVdKxollNS_iwn8WdUK-FVlbEIVaAC1V4zg"""
# url = 'https://management.azure.com/subscriptions/'+subid+'/resourcegroups?api-version=2017-05-10'
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
        print(Database[i]["displayName"])
        print(Database[i]["subscriptionId"])
        print(Database[i]["state"])


