
import requests
url = "https://lpnu.ua/"
response = requests.get(url).text.encode("utf-8")
print(response)