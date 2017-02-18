import urllib.request as ur
url = "https://www.google.co.in/?gws_rd=ssl"
conn = ur.urlopen(url)
print(conn)
data = conn.read()
print(data)
print("\n Connection Status ",conn.status)
print(conn.getheader("Content-Type"))