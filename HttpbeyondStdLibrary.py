import requests
url = "https://www.google.co.in/?gws_rd=ssl"
resp = requests.get(url)

print("Response 1@", resp)
print("Response 2#", resp.encoding)
print("Response 3$", resp.headers)
print("Response 2#",resp.text)
print(resp.__class__)