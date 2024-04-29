import http.client
import json

payload = json.dumps({"content": "<@558234730005397510> с др"})
count = 0
tokens = [str(input("token1: ")), str(input("token2: ")), str(input("token3: "))]

def sender():
    global count
    count = 0
    retry = 0
    # while True:
    for token in tokens:
            conn = http.client.HTTPSConnection("discord.com")
            conn.request("POST", "/api/v9/channels/1194216308603093114/messages", payload, headers={'Authorization': token, 'Content-Type': "application/json"})
            response = conn.getresponse()
            if response.status == 200:
                count+=1
                print(response.status, token, count)
            else:
                print(response.status, response.reason)
                retry += 1

            conn.close()

sender()