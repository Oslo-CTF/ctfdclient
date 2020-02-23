from pprint import pprint
from ctfdclient import CTFd

url = "http://192.168.1.85:8000"
user = "test"
pw = "Lollollol1"

if __name__ == "__main__":
    client = CTFd(url, user, pw, debug=True)

    challenge = client.challenges.create(name="Testing challenge", category="web", description="Hey try and solve this!", value=123, state="visible", type="standard")
    print("Created challenge:", challenge.name)
    
    flag = challenge.set_flag(client, "Oslo-CTF{flag}")
    print("Set flag:", flag["content"])

    upload = challenge.upload_file(client, "./testfile.jpg", "testfile.jpg")
    print("Upload file:", upload)
