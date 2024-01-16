import requests
GROUP_ID = "1115299825880024"
TOKEN = ""
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
