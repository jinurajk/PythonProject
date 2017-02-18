# Import the modules
import requests
import json

# Make it a bit prettier..
print("-" * 50)
print("This will show the Most Popular Videos on YouTube")
print("-" * 50)

# Get the feed  GDEshyq7wRY
r = requests.get("https://www.youtube.com/watch?v=bMt47wvK6u0&alt=jsonc")
r.text

print(r.text)
print("-" * 50)
# Convert it to a Python dictionary
data = json.loads(r.text)
print("From Youtubeee   ",data)

# Loop through the result.
for item in data['data']['items']:

    print("Video Title: %s" % (item['title']))

    print("Video Title: %s" % (item['title']))

    print("Video ID: %s" % (item['id']))

    print("Video Rating: %f" % (item['rating']))

    print("Embed URL: %s" % (item['player']['default']))

