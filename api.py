import requests
import json

def find(ip : str):
    url = f"https://coffee.alexflipnote.dev/{ip}?"
    result = requests.get(url).text
    return json.load(result)

if __name__=="__main__":
    print(find(input("ip address:")))