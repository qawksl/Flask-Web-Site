import requests
import json



def find():
    
    ds = requests.get("https://coffee.alexflipnote.dev/random.json").content
    image = json.loads(ds)["file"]
    return image
    



if __name__=="__main__":
    print(find(input("ip address:")))