import http.client
import json

payload = json.dumps({"content": "<@558234730005397510> с др"})

tokens = [str(Input("token1: ")), str(Input("token2: ")), str(Input("token3: "))]

def sender():
    retry = 0
    # while True:
    for token in tokens:
            conn = http.client.HTTPSConnection("discord.com")
            conn.request("POST", "/api/v9/channels/1041377842073710624/messages", payload, headers={'Authorization': token, 'Content-Type': "application/json"})
            response = conn.getresponse()

            if response.status == 200:
                print(response.status, token)
            else:
                print(response.status, response.reason)
                retry += 1

            conn.close()

sender()