import requests
GROUP_ID = "1115299825880024"
TOKEN = "EABiLaWq20EwBOya4HpGsFujVyZBpolomt88B0R4bmLeZBHxYulE4B33vQQ9n6TqYAu1SYhgYFi7UbYS7BJmlUUDKnMUxzuLyJwVvXfoeKj5CZCnZC75OwQ95mxS8KMsGFJpuFXSZAErpIS5Tc2PGUVM30vofeoy1VltGvYk0y6JWMp4lhCNH7uoUz13IkLBbc1xPiDEZANzwt912XODQZDZD"
URL="https://graph.facebook.com/"

with open("./addword.txt","r+") as file:
    data={
        "link":"http://facebook.com",
        "message":file.read(),
        "access_token":TOKEN
    }
r = requests.post(URL+GROUP_ID+"/feed",data=data)
if(r.status_code == 200):
    print("UPLOAD THANH CONG")
else:
    print("UPLOAD THANH THU")
